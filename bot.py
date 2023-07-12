from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import boto3

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self):
        session = boto3.Session(profile_name="default")
        self.lex_client = boto3.client('lexv2-runtime', region_name='us-east-1')
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text

        # Create a Lex client using your AWS credentials
        response = self.lex_client.recognize_text(
        botId='YQJMOL6FOF',
        botAliasId='UUT1BXOIRZ',
        localeId='en_US',
        sessionId=turn_context.activity.from_property.id,
        text=user_message
        )
    
        # Send the user message to Lex
        # response = self.lex_client.post_text(
        #     botName='Booking',
        #     botAlias='teams_alias',
        #     userId='turn_context.activity.from_property.id',
        #     inputText=user_message
        # )

        # Get the Lex response
        print(response)
        lex_response = response['messages'][0]['content']

        # Send the Lex response back to the user
        await turn_context.send_activity(lex_response)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
