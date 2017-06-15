from kahoot import Kahoot, kahootError
import json, base64, array
class receive:
    def __init__(self, kahootPointer):
        self.kahootPointer = kahootPointer
        self.variables = kahootPointer.variables
        self.queue = kahootPointer.queue
        self.send = kahootPointer.send
    def connect(self, response):
        if len(response) > 0:
            for i, x in enumerate(response):
                if x['channel'] != "/meta/connect":
                    self.runOrDrop(x)
    def testSession(self, r):
        try:
            if (r.status_code == 404):
                return False
            data = json.loads(r.text)
            if data['twoFactorAuth'] == False:
                chal_r = self.send.solveKahootChallenge(data['challenge'])
                if self.variables.debug:
                    print(chal_r)
                self.variables.setChallenge(chal_r.text)
                self.solveChallenge(r.headers['x-kahoot-session-token'])
                return True
            else:
                raise kahootError.kahootError('two factor not implemented')
        except Exception as e:
            raise kahootError.kahootError('receive.testSession error, r: '+str(r))
            return False
    def processclientId(self,r_text):
        self.variables.setclientId(r_text[0]["clientId"])
    def solveChallenge(self, kahoot_raw_session):
        kahoot_session_bytes = base64.b64decode(kahoot_raw_session)
        challenge_bytes = str(self.variables.kahootChallenge).encode("ASCII")
        bytes_list = []
        challenge_bytes_len = len(challenge_bytes)
        for i in range(len(kahoot_session_bytes)):
            bytes_list.append(kahoot_session_bytes[i] ^ challenge_bytes[i%challenge_bytes_len])
        kahootSession = array.array('B',bytes_list).tostring().decode("ASCII")
        self.variables.setKahootSession(kahootSession)
    def runOrDrop(self, *args):
        if self.variables.isUser:
            self.addTaskToQueue(*args)
    def addTaskToQueue(self, x):
        if x['channel'] == "/service/player":
            data = x['data']
            id_methods = {1:self.do_id_1, 2:self.do_id_2, 3:self.do_id_3, 4:self.do_id_4, 5:self.do_id_5, 7:self.do_id_7, 8:self.do_id_8, 10:self.do_id_10, 12:self.do_id_12, 13:self.do_id_13, 14:self.do_id_14} #51:self.do_id_51, 52:self.do_id_52, 53:self.do_id_53
            serviceID = int(data['id'])
            method = id_methods.get(serviceID, self.id_error)
            dataContent = json.loads(data['content'])
            if self.variables.debug:
                print("id:", serviceID, "\ndata:", dataContent)
            self.queue.add(method, dataContent)
        else:
            print(x['channel'])
    def id_error(self, dataContent):
        if self.variables.debug:
            print("id: ",dataContent['id'])
            raise kahootError.kahootError('cannot find ID from ' + self.variables.domain)
    def do_id_1(self, dataContent):
        self.variables.setCurrentQuestion(dataContent['questionIndex']-1)
        print("\nQuestion number: ", self.variables.getCurrentQuestionNumber())
    def do_id_2(self, dataContent):
        options = []
        self.variables.setCurrentQuestion(dataContent['questionIndex'])
        answer = self.ask_question(dataContent['answerMap'], dataContent['questionIndex']+1)
        self.send.sendAnswer(answer)
    def do_id_3(self, dataContent):
        print("End of quiz! \nYou came", self.ordinal(dataContent['rank']), "out of", dataContent['playerCount'],"players")
        print("You got", dataContent['totalScore'], "points")
        print("You got", dataContent['correctCount'], "Questions correct and", dataContent['incorrectCount'], "Questions incorect and had", dataContent['unansweredCount'], "Questions unanswered")
    def do_id_4(self, dataContent):
        self.variables.setCurrentQuestion(dataContent['questionNumber']-1)
        print("End of question", self.variables.getCurrentQuestionNumber())
    def do_id_5(self, dataContent):
        print('end')
    def do_id_7(self, dataContent):
        print('\n',dataContent['primaryMessage'])
    def do_id_8(self, dataContent):
        if dataContent['isCorrect']:
          print("Well Done, You got that question Correct!")
        else:
          print("Bad luck, You got that question incorrect!")
          if len(dataContent['correctAnswers']) > 1:
            print("The correct answers are:")
          else:
            print("The correct answer(s) are:")
          for x in dataContent['correctAnswers']:
            print(x)
        print("You got",dataContent['points'], "points\nand current score is", dataContent['totalScore'])
        print("You are", self.ordinal(dataContent['rank']))
        if dataContent['nemesis'] == None:
          print("Well done!")
        elif dataContent['totalScore'] == dataContent['nemesis']['totalScore']:
          print("Your tied with", dataContent['nemesis']['name'])
        elif dataContent['totalScore'] < dataContent['nemesis']['totalScore']:
          print("Your behind", dataContent['nemesis']['name'], "by", (dataContent['nemesis']['totalScore']- dataContent['totalScore']), "points")
    def do_id_9(self, dataContent):
        print("The name of this", dataContent['quizType'], "is", dataContent['quizName'], ". It has", len(dataContent['quizQuestionAnswers']), "Questions")
    def do_id_10(self, dataContent):
        print("end")
        #self.kahoot.end()
    def do_id_12(self, dataContent):
        print("finish")
    def do_id_13(self, dataContent):
        print(dataContent['primaryMessage'], "\n"+ dataContent['secondaryMessage'])
        print("That is the end of this", dataContent['quizType']," well done!")
        #self.kahoot.end()
    def do_id_14(self, dataContent):
        print("Connected\nYou joined this", dataContent['quizType'], "with the name", dataContent['playerName'])
    # def do_id_51(self, dataContent):
    #     print("Wrong Two factor code")
    #     self.twoFactorStarted = False
    # def do_id_52(self, dataContent):
    #     print("Two factor code correct")
    #     self.twoFactorSolved = True
    # def get_two_factor(self):
    #     if self.twoFactorPromptShown != True:
    #       print("Quiz needs a two factor code")
    #       print("Enter the first letter of the shape\n\n[t] for triangle\n[d] for Diamond\n[c] for circle\n[s] for square")
    #       print("Enetr it as one string,if it was a Triangle, Diamond, Circle and then Square")
    #       print("you would enter [tdcs]")
    #       self.twoFactorPromptShown = True
    #     else:
    #       print("enter two factor code again:")
    #     stringTwoFactor = str(input())
    #     if stringTwoFactor.isalpha():
    #       listTwoFactor = list(stringTwoFactor)
    #       if len(listTwoFactor) == 4:
    #         for i in range(len(listTwoFactor)):
    #           choices = {'t': '0', 'd': '1', 'c': '2', 's': '3'}
    #           listTwoFactor[i] = choices.get(listTwoFactor[i].lower(), '9')
    #         self.twoFactor = ''.join(listTwoFactor)
    #       else:
    #         print("Please enter a 4 letter code like [tdcs] excluding the brackets")
    #     else:
    #       print("Enter leters only please")
    # def do_id_53(self, dataContent):
    #     while not self.twoFactorSolved:
    #       if not self.twoFactorStarted:
    #         self.twoFactorStarted = True
    #         self.get_two_factor()
    #         self.send(self.make_two_factor_payload(self.twoFactor))
    def ask_question(self, ansMap, qNo):
        questionOptions = list(range(len(ansMap)))
        convOpts = {'r':0, 'b':1, 'y':2, 'g':3}
        print("please enter red, blue, yellow or green")
        print("enter as [r] [b] [y] or [g] and press [enter]")
        ansIn = input()
        ans = int(convOpts.get(ansIn, -1))
        if ans == -1:
            print("you entered an incorect answer")
        return ans


    def ask_question2(self, options, questionNo):
        options = list(options)
        questionNo = int(questionNo)
        print("List of options are:")
        for option in options:
            print(int(option)+1)
        try:
            answer = int(input("Enter your answer: ") - 1)
        except:
            answer = -1
        print("your entered an invalid input")
        if str(answer) in options:
            questionNo = questionNo - 1
            return int(answer)
        else:
            print("your answer is not is the list of options")
    def ordinal(self, n):
        if 10 <= n % 100 < 20:
            return str(n) + 'th'
        else:
           return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")
