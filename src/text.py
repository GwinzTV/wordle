

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


def title(text):
    text = fr'''
================================================================
|   {text}                                          |
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


def boxes(lst):
    _box = fr'''
._____.  ._____.  ._____.  ._____.  ._____.
|     |  |     |  |     |  |     |  |     |
|  {lst[0]}  |  |  {lst[1]}  |  |  {lst[2]}  |  |  {lst[3]}  |  |  {lst[4]}  |
|     |  |     |  |     |  |     |  |     |
'-----'  '-----'  '-----'  '-----'  '-----'
'''
    return _box
