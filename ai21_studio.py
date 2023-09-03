import ai21

def generate(prompt, ai21_api_key):
    ai21.api_key = ai21_api_key

    _prompt = """
    Write a tweet to promote an event for Shmolt, a food and more delivery company.
    ##
    Event: Christmas.
    Tweet: Oven broke in the last minute and you have no turkey? No need to panic, with Shmolt delivery it will be at your door step by Christmas eve!
    ##
    Event: Valentine's Day.
    Tweet: Order her roses using Shmolt, so you can have time to stop and smell the roses #Valentines
    ##
    Event: Summer Sale.
    Tweet: In this heat, why get out of the AC when you have 10% off of all Shmolt deliveries?
    ##
    Event: Mother's Day.
    Tweet:

    """
    
    response = ai21.Completion.execute(
        model="j2-mid",  # The engine to use for generation.
        prompt=_prompt + prompt,
        numResults=1,
        maxTokens=64,
        temperature=0.84,
        topKReturn=0,
        topP=1,
        countPenalty={
            "scale": 0.1,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        frequencyPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        presencePenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        stopSequences=["##"]
    )

    return response['completions'][0]['data']['text']
