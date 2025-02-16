from meta_ai_api import MetaAI
def weather():
    llm=MetaAI()
    place=input("Enter the place (i.e city with country): ")
    instruction=f'''
    you are a custom weather bot. You need to provide the weather information of given place 
    in proper format.
    - the given place is {place}
    if user input something else then you have to tell us that you are weather bot and you can only provide weather information
    '''
    response=llm.prompt(instruction)
    print(response["message"])
while(True):
    weather()
    print("Do you want to check weather of another place?")
    another=input("Enter yes or no: ")
    if another.lower()!="yes":
        break