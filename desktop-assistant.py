from tkinter import *
from google import genai
import creds
import webbrowser


def web_search(query):
    if isinstance(query, list):
        query = " ".join(query)

    #api response
    key= creds.google_api_key
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=query
    )

    answer=Tk()
    answer.title("Response")
    text=Text(answer)
    text.insert(END, response.text)
    text.pack()

    answer.mainloop()

def youtube(query):
    if len(query) == 1:
        webbrowser.open("https://www.youtube.com/")
    else:
        webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(query[1:]))

def work(self):
    user_input = list(entry.get().split())
    window.destroy()
    if user_input == []:
        return
    if user_input[0][0]== "/":
        if user_input[0] == "/yt":
            youtube(user_input)
    else:
        web_search(user_input)



window= Tk()
entry=Entry(window, width=50, bg="#6c6867", fg="black", font=("Arial", 20))
entry.pack()
window.bind("<Return>",work)
window.title("Desktop Assistant")
window.mainloop()
