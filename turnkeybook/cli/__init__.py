from turnkeybook.neuralnetworks.communication import ChatGPTCommunicator

def entrypoint() -> None:
    communicator = ChatGPTCommunicator()
    while True:
        result = communicator.request(input())
        print(f" NN> {result}")
        print("You> ", end="")

