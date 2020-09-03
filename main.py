"""
Sharda Raina
Main file containing code for the covid bot.
"""
import tkinter as tk
# dictionary that will contain all user info
user_info = dict()


class Checkbox(tk.Frame):
    # checkbox class, to make checklists
    def __init__(self, parent=None, picks=[]):
        tk.Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)
            chk.pack()
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master=None)
        self.master = master
        self.pack()
        intro_frame = tk.Frame(master)
        self.main_frame = tk.Frame(master)
        self.disclaimer = tk.Label(
            intro_frame,
            text="This is not a doctor's diagnosis, just an assistant bot.",
            bg='red',
            fg='white')
        self.disclaimer.pack()

        intro_text = """Hello, I am a Covid Assistance Bot!
        Answering these questions will guide me in assisting
        you and providing further information and care.
        Although this is not a medical diagnosis, I can
        recommend treatment or provide you with useful information!"""
        intro = tk.Label(intro_frame, text=intro_text)
        intro.pack()
        intro_frame.pack()
        self.main_frame.pack()
        self.step1()

    def step1(self):
        # step 1 - just disclaimer, accept the disclaimer
        self.button1 = tk.Button(self.main_frame)
        self.button1["text"] = "I understand"
        self.button1["command"] = self.step2
        self.button1.pack(side="left")
        self.quit = tk.Button(
            self.main_frame,
            text="QUIT",
            fg="red",
            command=self.master.destroy)
        self.quit.pack(side="bottom")

    def step2(self):
        # step2 emergency checklist
        user_info['accepted'] = 'yes'
        # once user clicks accept button, it disappears
        self.button1.destroy()
        self.disclaimer.destroy()

        self.severe = tk.Text(self.main_frame, height=3)
        severetext = """Do you have any of these severe symptoms? If so, please call 911 immediately"""
        self.severe.insert(tk.INSERT, severetext)
        self.severe.pack()
        self.checklist6 = Checkbox(self.main_frame, [
            'Bluish lips or face',
            'Severe and constant pain or pressure in the chest',
            'Extreme difficulty breathing (such as gasping for air or being unable to talk without catching your breath)',
            'Severe and constant dizziness or lightheadedness',
            'New Serious disorientation (acting confused)',
            'Unconscious or very difficult to wake up',
            'Slurred speech or difficulty speaking (new or worsening)',
            'Seizures',
            'Signs of low blood pressure (too weak to stand, light headed, feeling cold, pale, clammy skin)',
            'Low oxygen level--if you can test for that'])
        self.checklist6.pack()

        self.button2 = tk.Button(self.main_frame)
        self.button2["text"] = "Next"
        self.button2.pack(side="bottom")
        self.button2["command"] = self.step3

    def step3(self):
        self.severeresponse = self.checklist6.state()
        severe_list = list(self.severeresponse)
        if 1 in severe_list:
            self.severe.destroy()
            self.button2.destroy()
            self.checklist6.destroy()
            self.call911 = tk.Text(self.main_frame, height=3)
            text_911 = "Please call 911! Your symptoms could be deadly."
            self.call911.insert(tk.INSERT, text_911)
            self.call911.pack()

        else:
            self.severe.destroy()
            self.checklist6.destroy()

            self.age = tk.Text(self.main_frame, height=3)
            agetext = "What age range are you in?"
            self.age.insert(tk.INSERT, agetext)
            self.age.pack(side="top")
            self.checklist1 = Checkbox(self.main_frame,
                                   ['0-20', '20-40', '40-60', '60-80', '80+'])
            self.checklist1.pack()
        
            self.button2["command"] = self.step4

    def step4(self):
        self.age_response = self.checklist1.state()
        user_info["age"] = list(self.age_response)

        self.checklist1.destroy()
        self.age.destroy()

        self.gender = tk.Text(self.main_frame, height=3)
        gendertext = "What gender do you identify as?"
        self.gender.insert(tk.INSERT, gendertext)
        self.gender.pack()
        self.checklist2 = Checkbox(self.main_frame,
                                   ['Female', 'Male', 'Nonbinary', 'Other'])
        self.checklist2.pack(side="top")
        self.button2["command"] = self.step5

    def step5(self):
        self.gender_response = self.checklist2.state()
        user_info["gender"] = list(self.gender_response)

        self.checklist2.destroy()
        self.gender.destroy()

        self.button2["command"] = self.step5
        self.location = tk.Text(self.main_frame, height=3)
        locationtext = "Where are you located?"
        self.location.insert(tk.INSERT, locationtext)
        self.location.pack()
        self.checklist3 = Checkbox(self.main_frame, [
            'USA', 'Canada', 'Mexico',
            'Europe', 'South America', 'Africa', 'East Asia', 'West Asia',
            'Southeast Asia', 'Australia'
        ])
        self.checklist3.pack()
        self.button2["command"] = self.step6

    def step6(self):
        self.location_response = self.checklist3.state()
        user_info["location"] = list(self.location_response)

        self.checklist3.destroy()
        self.location.destroy()

        self.contact = tk.Text(self.main_frame, height=3)
        contacttext = """Have you been in contact with people not in
        your living space in the past 14 days? (i.e. meeting friends,
        going to a restaurant, grocery shopping)"""
        self.contact.insert(tk.INSERT, contacttext)
        self.contact.pack()
        self.checklist4 = Checkbox(self.main_frame, ['yes', 'no'])
        self.checklist4.pack()
        self.button2["command"] = self.step7

    def step7(self):
        self.contact_response = self.checklist4.state()
        user_info["contact"] = list(self.contact_response)

        self.checklist4.destroy()
        self.contact.destroy()

        self.flu = tk.Text(self.main_frame, height=3)
        flutext = """Have you gotten the flu vaccine this year?"""
        self.flu.insert(tk.INSERT, flutext)
        self.flu.pack()
        self.checklist5 = Checkbox(self.main_frame, ['yes', 'no'])
        self.checklist5.pack()
        self.button2["command"] = self.step8

    def step8(self):
        self.flu_response = self.checklist5.state()
        user_info["flu"] = list(self.flu_response)

        self.checklist5.destroy()
        self.flu.destroy()

        self.normal = tk.Text(self.main_frame, height=3)
        normaltext = "Do you have any of these symptoms?"
        self.normal.insert(tk.INSERT, normaltext)
        self.normal.pack()
        self.checklist7 = Checkbox(self.main_frame, [
            'Fever or chills', 'Cough',
            'Shortness of breath or difficulty breathing', 'Fatigue',
            'Muscle or body aches', 'Headache', 'New loss of taste or smell',
            'Sore throat', 'Congestion or runny nose', 'Nausea or vomiting',
            'Diarrhea'])
        self.checklist7.pack()
        self.button2["command"] = self.step9

    def step9(self):
        self.symptom_response = self.checklist7.state()

        user_info["symptom"] = list(self.symptom_response)

        self.checklist7.destroy()
        self.normal.destroy()

        self.diseases = tk.Text(self.main_frame, height=3)
        diseasetext = "Do any of these risk factors apply to you?"
        self.diseases.insert(tk.INSERT, diseasetext)
        self.diseases.pack()
        self.checklist8 = Checkbox(self.main_frame, [
            'Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease), cystic fibrosis, or pulmonary fibrosis',
            'Serious heart condition, such as heart failure, coronary artery disease, or cardiomyopathy',
            'Weakened immune system or taking medications that may cause immune suppression',
            'Obesity', 'Diabetes, chronic kidney disease, or liver disease',
            'High blood pressure',
            'Blood disorder, such as sickle cell disease or thalassemia',
            'Cerebrovascular disease or neurologic condition, such as stroke or dementia',
            'Smoking', 'Pregnancy'])

        self.checklist8.pack()
        self.disease_response = self.checklist8.state()
        self.button2["command"] = self.step10

    def step10(self):
        self.disease_response = self.checklist8.state()
        user_info["disease"] = list(self.disease_response)

        self.checklist8.destroy()
        self.diseases.destroy()
        faq_text = """Covid 19 may be carried regardless of displaying symptoms.
Please wear a mask and practice social distancing.

        Here are useful links for learning more about Covid-19!
        Please copy and paste these into your browser.
        https://coronavirus.jhu.edu/map.html
        https://www.cdc.gov/coronavirus/2019-ncov/index.html
        https://www.who.int/health-topics/coronavirus#tab=tab_1
        https://www.cdc.gov/flu/symptoms/flu-vs-covid19.htm
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7194613/ 
        
        Thank you for using this Covid-19 Bot!"""
        self.faq = tk.Text(self.main_frame, height=15)
        self.faq.insert(tk.INSERT, faq_text)

        if 1 in user_info["symptom"]:
            response_text = """Based on your symptoms, you may have Covid-19. Please call your doctor to get tested! """
            smell_text = """Loss of taste or smell is unique to Covid-19. You are extremely likely to have Covid-19. """
            distance_text = """Based on your response of having contact with others, this adds to your chances of having Covid-19. """
            disease_text = """Based on your response of potential risk factors, this adds to your chances of Covid-19 complications."""
            self.response = tk.Text(self.main_frame, height=6)
            self.response.insert(tk.INSERT, response_text)
            self.response.pack()
            self.faq.pack()
            if user_info["symptom"][6] == 1:
                self.response.insert(tk.INSERT, smell_text)
                self.response.pack()
            if user_info["contact"][0] == 1:
                self.response.insert(tk.INSERT, distance_text)
                self.response.pack()
            if 1 in user_info["disease"]:
                self.response.insert(tk.INSERT, disease_text)
                self.response.pack()

        else:
            no_response_text = "Since you did not check any symptoms, here is relevant information."
            self.noresponse = tk.Text(self.main_frame, height=3)
            self.noresponse.insert(tk.INSERT, no_response_text)
            self.noresponse.pack()
            self.faq.pack()

        self.button2.destroy()


root = tk.Tk()
c_bot = App(master=root)
c_bot.master.title("Covid-19 Diagnostic Assistant Bot")
c_bot.mainloop()
