from abc import abstractmethod, ABC


class OpenaiChatbotDomainService(ABC):
    @abstractmethod
    def generateRecipe(self, userSendMessage):
        pass

    @abstractmethod
    def getGeneratedVoice(self, chatbotMessage, voiceActor):
        pass