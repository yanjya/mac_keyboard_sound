from pynput import keyboard
import pygame

# 初始化 pygame
pygame.init()

# 加載音樂
pygame.mixer.music.load('/Users/jie/Documents/pdf_chat/21.mp3')

# 定義一個函數來處理鍵盤按鍵事件
def on_press(key):
    pygame.mixer.music.play()

# 使用 pynput.keyboard.Listener 來監聽鍵盤事件
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()