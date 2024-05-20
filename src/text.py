def won(attempt):
    text = f"\nCongrats! You got the Wordle in {attempt} tries"
    return text


def lost():
    text = "Unlucky, you did not solve the Wordle this time around!\n"
    return text


def replay():
    text = "\nWant to play again? Hit 'Enter' to continue or enter "
    text += "'q' to Quit "
    return text


def title():
    text = r'''
================================================================
|   Welcome to ...                                             |
|                                                              |
|   $$\      $$\                           $$\ $$\             |
|   $$ | $\  $$ |                          $$ |$$ |            |
|   $$ |$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$$ |$$ | $$$$$$\    |
|   $$ $$ $$\$$ |$$  __$$\ $$  __$$\ $$  __$$ |$$ |$$  __$$\   |
|   $$$$  _$$$$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |$$$$$$$$ |  |
|   $$$  / \$$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$   ____|  |
|   $$  /   \$$ |\$$$$$$  |$$ |      \$$$$$$$ |$$ |$$$$$$$\    |
|   \__/     \__| \______/ \__|       \_______|\__|\_______|   |
|                                                              |
|                                Created By Developer: GwinzTV |
================================================================
'''
    return text
