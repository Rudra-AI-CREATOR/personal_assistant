import pyttsx3 as r
import math
import webbrowser
import speech_recognition as sr
import datetime
import pywhatkit as pyk
print("to open anything on website just say [open youtube , open flipkart etc")
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing.....")
            data = recognizer.recognize_google(audio)
          # print(data)
            return data
        except sr.UnknownValueError:
            print("re try....")
def speechtx(x):
    engine = r.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',  voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate' ,100)
    engine.say(x)
    engine.runAndWait()
xq = 1
if __name__ == '__main__':
    while xq == 1:
        data1 = sptext().lower()
        website = "https://www.google.com/"
        if " your name" in data1:
            name = "my name rudra personal A.I assistance"
            speechtx(name)
        elif "afghanistan" in data1:
            answer = "Kabul"
            speechtx(answer)
        elif "india" in data1:
            answer = "new delhi"
            speechtx(answer)
        elif "algeria" in data1:
            answer = "Algiers"
            speechtx(answer)
        elif "andorra" in data1:
            answer = "Andorra la Vella"
            speechtx(answer)
        elif "angola" in data1:
            answer = "Luanda"
            speechtx(answer)
        elif "antigua and Barbuda" in data1:
            answer = "St. John's"
            speechtx(answer)
        elif "argentina" in data1:
            answer = "Buenos Aires"
            speechtx(answer)
        elif "armenia" in data1:
            answer = "Yerevan"
            speechtx(answer)
        elif "australia" in data1:
            answer = "Canberra"
            speechtx(answer)
        elif "austria" in data1:
            answer = "Vienna"
            speechtx(answer)
        elif "azerbaijan" in data1:
            answer = "Baku"
            speechtx(answer)
        elif "bahamas" in data1:
            answer = "Nassau"
            speechtx(answer)
        elif "bahrain" in data1:
            answer = "Manama"
            speechtx(answer)
        elif "bangladesh" in data1:
            answer = "Dhaka"
            speechtx(answer)
        elif "barbados" in data1:
            answer = "Bridgetown"
            speechtx(answer)
        elif "belarus" in data1:
            answer = "Minsk"
            speechtx(answer)
        elif "belgium" in data1:
            answer = "Brussels"
            speechtx(answer)
        elif "belize" in data1:
            answer = "Belmopan"
            speechtx(answer)
        elif "benin" in data1:
            answer = "Porto-Novo"
            speechtx(answer)
        elif "bhutan" in data1:
            answer = "Thimphu"
            speechtx(answer)
        elif "bolivia" in data1:
            answer = "Sucre"
            speechtx(answer)
        elif "bosnia and herzegovina" in data1:
            answer = "Sarajevo"
            speechtx(answer)
        elif "botswana" in data1:
            answer = "Gaborone"
            speechtx(answer)
        elif "brazil" in data1:
            answer = "Brasília"
            speechtx(answer)
        elif "brunei" in data1:
            answer = "Bandar Seri Begawan"
            speechtx(answer)
        elif "bulgaria" in data1:
            answer = "Sofia"
            speechtx(answer)
        elif "burkina Faso" in data1:
            answer = "Ouagadougou"
            speechtx(answer)
        elif "burundi" in data1:
            answer = "Bujumbura"
            speechtx(answer)
        elif "cambodia" in data1:
            answer = "Phnom Penh"
            speechtx(answer)
        elif "cameroon" in data1:
            answer = "Yaoundé"
            speechtx(answer)
        elif "canada" in data1:
            answer = "Ottawa"
            speechtx(answer)
        elif "central african republic" in data1:
            answer = "Bangui"
            speechtx(answer)
        elif "chad" in data1:
            answer = "N'Djamena"
            speechtx(answer)
        elif "chile" in data1:
            answer = "Santiago"
            speechtx(answer)
        elif "china" in data1:
            answer = "Beijing"
            speechtx(answer)
        elif "colombia" in data1:
            answer = "Bogotá"
            speechtx(answer)
        elif "comoros" in data1:
            answer = "Moroni"
            speechtx(answer)
        elif "congo" in data1:
            answer = "Brazzaville"
            speechtx(answer)
        elif "costa rica" in data1:
            answer = "San José"
            speechtx(answer)
        elif "côte d'ivoire" in data1:
            answer = "Yamoussoukro"
            speechtx(answer)
        elif "croatia" in data1:
            answer = "Zagreb"
            speechtx(answer)
        elif "cuba" in data1:
            answer = "Havana"
            speechtx(answer)
        elif "cyprus" in data1:
            answer = "Nicosia"
            speechtx(answer)
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%P")
            speechtx(time)
        elif 'open' in data1:
            w = 0
            for i in data1:
                # print(i)
                if i == " ":
                    w += 1
            if w == 1:
                op = (data1[5::])
                pyk.search(op)
        elif 'trigonometry' in data1:
            print("Trigonometric Values Calculator")
            print("---------------------------------")
            # Get the user input for the angle in degrees
            angle_degrees = float(input("Enter the angle in degrees: "))
            # Convert the angle from degrees to radians
            angle_radians = math.radians(angle_degrees)
            # Calculate the trigonometric values
            sine = math.sin(angle_radians)
            cosine = math.cos(angle_radians)
            tangent = math.tan(angle_radians)
            cosecant = 1 / math.sin(angle_radians)
            secant = 1 / math.cos(angle_radians)
            cotangent = 1 / math.tan(angle_radians)
            # Print the results
            print(f"Sin({angle_degrees}°) = {sine:.4f}")
            print(f"Cos({angle_degrees}°) = {cosine:.4f}")
            print(f"Tan({angle_degrees}°) = {tangent:.4f}")
            print(f"Csc({angle_degrees}°) = {cosecant:.4f}")
            print(f"Sec({angle_degrees}°) = {secant:.4f}")
            print(f"Cot({angle_degrees}°) = {cotangent:.4f}")
            speechtx(f"Sin({angle_degrees}°) = {sine:.4f}")
            speechtx(f"Cos({angle_degrees}°) = {cosine:.4f}")
            speechtx(f"Tan({angle_degrees}°) = {tangent:.4f}")
            speechtx(f"Csc({angle_degrees}°) = {cosecant:.4f}")
            speechtx(f"Sec({angle_degrees}°) = {secant:.4f}")
            speechtx(f"Cot({angle_degrees}°) = {cotangent:.4f}")
        else:
            print("thanks")
            break
