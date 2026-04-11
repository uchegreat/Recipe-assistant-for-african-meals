from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import openai


class RecipeChatbotView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_message = request.data.get("message", "")

        if not user_message:
            return Response({"error": "Message is required"}, status=400)

        try:
            client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert in African cuisine. "
                            "Only answer questions related to African meals, recipes, and cooking methods. "
                            "If a user asks about non-African meals, politely redirect them to ask about African dishes."
                        ),
                    },
                    {"role": "user", "content": user_message}
                ],
                temperature=0.9,  #  Higher creativity
                top_p=0.95,  #  More varied responses
                max_tokens=800,  # More detailed explanations
                frequency_penalty=0.5,  #  Reduce repetition
                presence_penalty=0.6  #  Encourage diverse output
            )

            chatbot_reply = response.choices[0].message.content

            return Response({"reply": chatbot_reply})

        except openai.OpenAIError as e:
            return Response({"error": str(e)}, status=500)















