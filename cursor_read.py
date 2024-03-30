import pyautogui as pg

def start_recording(n, file_path='recorded_data.txt'):
    try:
        with open(file_path, 'w') as file:
            for i in range(60 * n):
                x, y = pg.position()
                file.write(f'{x},{y}\n')
                pg.sleep(0.010)
        print(f'Recording completed. Data saved to {file_path}')
    except Exception as e:
        print(f'Error saving recorded data: {e}')

def play_recording(file_path='recorded_data.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()[::-1] 
            for line in lines:
                x, y = map(int, line.strip().split(','))
                pg.click(x, y)
        print(f'Playback completed from {file_path}')
    except Exception as e:
        print(f'Error playing recorded data: {e}')

def main():
    n = int(input('Enter recording time in seconds: '))
    timer = 5
    for i in range(timer):
        print(f'Recording will start in {timer - i} seconds')
        pg.sleep(1)
    print('GO')
    start_recording(n)
    play_option = input('Do you want to play the recorded data? (y/n): ').lower()
    if play_option == 'y':
        play_recording()

if __name__ == "__main__":
    main()
