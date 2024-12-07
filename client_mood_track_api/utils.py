import json


class CommentProcessor:

    def __init__(self, data):
        self.data = data

    def process_comment(self):
        print("Processing comment...")
        data = self.analyze_comment_ai()
        # send to db
        try:
            return True
        except:
            return False

    def analyze_comment_ai(self):
        user_name = self.data.get("userName")
        print(f"Analyzing {user_name}`s comment")
        # implement chat gpt api
