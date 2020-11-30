time: int = int(input('Enter time in seconds: '))
hours: int = time // 3600
minutes: int = (time // 60) - (hours * 60)
seconds: int = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
