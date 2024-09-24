from itertools import count
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        if not isinstance(title, str):
            print('Введите название видео.')
        else:
            self.title = title
        if not isinstance(duration, int):
            print('Введите продолжительность видео (в секундах).')
        else:
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = User
    current_user.nickname = ''
    current_user.password = 0
    current_user.age = 0

    def add(Video, *args):
        for video_in in args:
            # print('args - ', video_in.title)
            UrTube.videos.append(video_in)

    def get_videos(self, find_line):
        video_out = []
        for video_find in UrTube.videos:
            if video_find.title.lower().find(find_line.lower()) >= 0:
                video_out.append(video_find.title)
        return video_out

    def register(self, *args):
        name = args[0]
        if UrTube.users.count(name) > 0:
            print(f'Пользователь {name} уже существует')
            return
        else:
            UrTube.current_user.nickname = args[0]
            UrTube.current_user.password = hash(args[1])
            UrTube.current_user.age = args[2]
            UrTube.users.append(UrTube.current_user.nickname)
            UrTube.users.append(UrTube.current_user.password)
            UrTube.users.append(UrTube.current_user.age)


    def watch_video(self, video_demand):
        if UrTube.current_user.age == 0:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            video_in = UrTube.get_videos(self, video_demand)
            # print('video_in - ', video_in)
            for video_find in UrTube.videos:
                if video_find.title.lower().find(video_in[0].lower()) >= 0:
                    adult_mode_find = video_find.adult_mode
                    duration_find = video_find.duration
                    break

            if UrTube.current_user.age < 18 and adult_mode_find == True:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            else:
                for i_vid in range(duration_find):
                    print(i_vid + 1, end=' ')
                    sleep(1)

                print('Конец видео')






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
