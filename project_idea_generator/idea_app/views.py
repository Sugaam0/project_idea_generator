import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import IdeaForm
import markdown
from .models import ProjectIdea
from groq import Groq, RateLimitError, GroqError
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


def home_view(request):
    return render(request, 'home.html')

# Function to call Groq API
def generate_project_idea(prompt):
    try:
        client = Groq(api_key=groq_api_key)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{
                "role": "user",
                "content": f"{prompt}\n\nProvide 5 project ideas as a numbered list with:\n- **Project Name**\n- **Description**\n- **How to Do It**"
            }]
        )
        return response.choices[0].message.content.strip()
    except RateLimitError:
        return "Rate limit exceeded. Try again later."
    except GroqError as e:
        return f"Error generating idea: {e}"

# View to render form and display result
@login_required
def generate_ideas(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user

            prompt = (
                f"Generate 5 {idea.type} level project ideas "
                f"in the field of {idea.field}, genre {idea.genre}."
            )
            if idea.additional_info:
                prompt += f" Additional context: {idea.additional_info}"

            result = generate_project_idea(prompt)

            # Convert markdown to HTML
            idea.generated_ideas = markdown.markdown(result)
            idea.save()

            return render(request, 'Idea/result.html', {'idea': idea})
    else:
        form = IdeaForm()
    return render(request, 'Idea/idea.html', {'form': form})

def about(request):
    return render(request, 'Idea/about.html')