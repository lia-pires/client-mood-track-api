import json

from client_mood_track_api.openai import OpenAi


class CommentProcessor:

    def __init__(self, data):
        self.data = data

    def process_comment(self):
        openai = OpenAi()
        print("Processing comment...")
        try:
            analyzed_data = openai.analyze_comment_ai(self.data)
            # implement mongodb
            return True

        except:
            return False
