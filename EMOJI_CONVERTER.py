# This is a simple emoji converter that replaces certain words in a message with their corresponding emojis.
message=input("Enter your message: ")
msg=message.replace("happy", "😊").replace("sad", "😢").replace("love", "❤️").replace("angry", "😠")
print(msg)
