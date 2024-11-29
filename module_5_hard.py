from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user_ in self.users:
            if nickname == user_.nickname and hash(password) == user_.password:
                self.current_user = user_
                break

    def register(self, nickname, password, age):
        for user_ in self.users:
            if nickname == user_.nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        self.users.append(u := User(nickname, password, age))
        self.current_user = u

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video_ in args:
            if video_ not in self.videos:
                self.videos.append(video_)

    def get_videos(self, search: str):
        l = []
        for video_ in self.videos:
            if search.lower() in video_.title.lower():
                l.append(video_.title)

        return l

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video_ in self.videos:
                if title == video_.title:
                    if video_.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for t in range(video_.time_now + 1, video_.duration + 1):
                            sleep(1)
                            print(t, end = " ")
                        print("Конец видео")
                    break

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')

