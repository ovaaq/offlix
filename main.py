import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import BorderImage
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer, VideoPlayerAnnotation
from kivy.uix.video import Video
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
import time




store = JsonStore('info.json')


# 1 -> Disney Princess
# 2 -> Animations
# 3 -> Wizarding World
# 4 -> Marvel Studio
# 5 -> Fantasy
# 6 -> Action
# 7 -> Science Fiction
#
#
#
#store.put("60",
#id="60",
#name="Raiders of the Lost Ark",
#description="In 1936, archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before Adolf Hitler's Nazis can obtain its awesome powers.")








def movieName(id):
    return store.get(id)['name']

def movieDescription(id):
    return store.get(id)['description']

def loadMovie(id):
    return store.get(id)['source']

def forward():
    pass

class ScreenMenu(Screen):

    def __init__(self, **kwargs):
        super().__init__()


        global carousel01, carousel02, carousel03, carousel04, carousel05
        global carousel11, carousel12, carousel13, carousel14, carousel15
        global carousel21, carousel22, carousel23, carousel24, carousel25
        global carousel31, carousel32, carousel33, carousel34, carousel35
        global carousel41, carousel42, carousel43, carousel44, carousel45
        global carousel51, carousel52, carousel53, carousel54, carousel55
        global carousel61, carousel62, carousel63, carousel64, carousel65

        global hugeCarousel
        global currentMovie
        global description

        wrapper = BoxLayout(orientation="vertical")

        moviesAndCategory = BoxLayout(orientation="vertical")

        movieInfo = BoxLayout(orientation="vertical")

##################################(   HUGE CAROUSEL NO1   )#############################################

        carousel01 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel02 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel03 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel04 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel05 = Carousel(direction='right', loop="True", anim_type="linear")

        count1 = 5

        for i in range(count1):
            src = "1" + str(i) + ".jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel01.add_widget(image)

        for i in range(count1):
            src = "1" + str(i) + ".jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel02.add_widget(image)

        for i in range(count1):
            src = "1" + str(i) + ".jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel03.add_widget(image)

        for i in range(count1):
            src = "1" + str(i) + ".jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel04.add_widget(image)

        for i in range(count1):
            src = "1" + str(i) + ".jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel05.add_widget(image)

        carousel01.index = 0
        carousel02.index = 1
        carousel03.index = 2
        carousel04.index = 3
        carousel05.index = 4

        movieWrapper1 = BoxLayout(orientation="vertical")

        category1 = Label(text="Disney Princess", font_size = "45", bold="True")
        category1.size_hint = (1, 0.2)
        category1.pos_hint = {'right': 0.6}

        movies1 = BoxLayout()

        movies1.add_widget(carousel01)
        movies1.add_widget(carousel02)
        movies1.add_widget(carousel03)
        movies1.add_widget(carousel04)
        movies1.add_widget(carousel05)

        movieWrapper1.add_widget(category1)
        movieWrapper1.add_widget(movies1)

##################################(   HUGE CAROUSEL NO2   )#############################################

        carousel11 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel12 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel13 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel14 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel15 = Carousel(direction='right', loop="True", anim_type="linear")

        count2 = 26

        for i in range(count2):
            src = "2" + str(i) + ".jpg"
            image2 = AsyncImage(source=src, allow_stretch=True)
            carousel11.add_widget(image2)

        for i in range(count2):
            src = "2" + str(i) + ".jpg"
            image2 = AsyncImage(source=src, allow_stretch=True)
            carousel12.add_widget(image2)

        for i in range(count2):
            src = "2" + str(i) + ".jpg"
            image2 = AsyncImage(source=src, allow_stretch=True)
            carousel13.add_widget(image2)

        for i in range(count2):
            src = "2" + str(i) + ".jpg"
            image2 = AsyncImage(source=src, allow_stretch=True)
            carousel14.add_widget(image2)

        for i in range(count2):
            src = "2" + str(i) + ".jpg"
            image2 = AsyncImage(source=src, allow_stretch=True)
            carousel15.add_widget(image2)

        carousel11.index = 0
        carousel12.index = 1
        carousel13.index = 2
        carousel14.index = 3
        carousel15.index = 4

        movieWrapper2 = BoxLayout(orientation="vertical")

        category2 = Label(text="Animation", font_size = "45", bold="True")
        category2.size_hint = (1, 0.2)
        category2.pos_hint = {'right': 0.6}

        movies2 = BoxLayout()

        movies2.add_widget(carousel11)
        movies2.add_widget(carousel12)
        movies2.add_widget(carousel13)
        movies2.add_widget(carousel14)
        movies2.add_widget(carousel15)

        movieWrapper2.add_widget(category2)
        movieWrapper2.add_widget(movies2)

##################################(   HUGE CAROUSEL NO3   )#############################################

        carousel21 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel22 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel23 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel24 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel25 = Carousel(direction='right', loop="True", anim_type="linear")

        count3 = 9

        for i in range(count3):
            src = "3" + str(i) + ".jpg"
            image3 = AsyncImage(source=src, allow_stretch=True)
            carousel21.add_widget(image3)

        for i in range(count3):
            src = "3" + str(i) + ".jpg"
            image3 = AsyncImage(source=src, allow_stretch=True)
            carousel22.add_widget(image3)

        for i in range(count3):
            src = "3" + str(i) + ".jpg"
            image3 = AsyncImage(source=src, allow_stretch=True)
            carousel23.add_widget(image3)

        for i in range(count3):
            src = "3" + str(i) + ".jpg"
            image3 = AsyncImage(source=src, allow_stretch=True)
            carousel24.add_widget(image3)

        for i in range(count3):
            src = "3" + str(i) + ".jpg"
            image3 = AsyncImage(source=src, allow_stretch=True)
            carousel25.add_widget(image3)

        carousel21.index = 0
        carousel22.index = 1
        carousel23.index = 2
        carousel24.index = 3
        carousel25.index = 4

        movieWrapper3 = BoxLayout(orientation="vertical")

        category3 = Label(text="Wizarding World", font_size = "45", bold="True")
        category3.size_hint = (1, 0.2)
        category3.pos_hint = {'right': 0.6}

        movies3 = BoxLayout()

        movies3.add_widget(carousel21)
        movies3.add_widget(carousel22)
        movies3.add_widget(carousel23)
        movies3.add_widget(carousel24)
        movies3.add_widget(carousel25)

        movieWrapper3.add_widget(category3)
        movieWrapper3.add_widget(movies3)

##################################(   HUGE CAROUSEL NO4   )#############################################

        carousel31 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel32 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel33 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel34 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel35 = Carousel(direction='right', loop="True", anim_type="linear")

        count4 = 22

        for i in range(count4):
            src = "4" + str(i) + ".jpg"
            image4 = AsyncImage(source=src, allow_stretch=True)
            carousel31.add_widget(image4)

        for i in range(count4):
            src = "4" + str(i) + ".jpg"
            image4 = AsyncImage(source=src, allow_stretch=True)
            carousel32.add_widget(image4)

        for i in range(count4):
            src = "4" + str(i) + ".jpg"
            image4 = AsyncImage(source=src, allow_stretch=True)
            carousel33.add_widget(image4)

        for i in range(count4):
            src = "4" + str(i) + ".jpg"
            image4 = AsyncImage(source=src, allow_stretch=True)
            carousel34.add_widget(image4)

        for i in range(count4):
            src = "4" + str(i) + ".jpg"
            image4 = AsyncImage(source=src, allow_stretch=True)
            carousel35.add_widget(image4)

        carousel31.index = 0
        carousel32.index = 1
        carousel33.index = 2
        carousel34.index = 3
        carousel35.index = 4

        movieWrapper4 = BoxLayout(orientation="vertical")

        category4 = Label(text="Marvel Studios", font_size = "45", bold="True")
        category4.size_hint = (1, 0.2)
        category4.pos_hint = {'right': 0.6}

        movies4 = BoxLayout()

        movies4.add_widget(carousel31)
        movies4.add_widget(carousel32)
        movies4.add_widget(carousel33)
        movies4.add_widget(carousel34)
        movies4.add_widget(carousel35)

        movieWrapper4.add_widget(category4)
        movieWrapper4.add_widget(movies4)

##################################(   HUGE CAROUSEL NO5   )#############################################

        carousel41 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel42 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel43 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel44 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel45 = Carousel(direction='right', loop="True", anim_type="linear")

        count5 = 11

        for i in range(count5):
            src = "5" + str(i) + ".jpg"
            image5 = AsyncImage(source=src, allow_stretch=True)
            carousel41.add_widget(image5)

        for i in range(count5):
            src = "5" + str(i) + ".jpg"
            image5 = AsyncImage(source=src, allow_stretch=True)
            carousel42.add_widget(image5)

        for i in range(count5):
            src = "5" + str(i) + ".jpg"
            image5 = AsyncImage(source=src, allow_stretch=True)
            carousel43.add_widget(image5)

        for i in range(count5):
            src = "5" + str(i) + ".jpg"
            image5 = AsyncImage(source=src, allow_stretch=True)
            carousel44.add_widget(image5)

        for i in range(count5):
            src = "5" + str(i) + ".jpg"
            image5 = AsyncImage(source=src, allow_stretch=True)
            carousel45.add_widget(image5)

        carousel41.index = 0
        carousel42.index = 1
        carousel43.index = 2
        carousel44.index = 3
        carousel45.index = 4

        movieWrapper5 = BoxLayout(orientation="vertical")

        category5 = Label(text="Fantasy", font_size = "45", bold="True")
        category5.size_hint = (1, 0.2)
        category5.pos_hint = {'right': 0.6}

        movies5 = BoxLayout()

        movies5.add_widget(carousel41)
        movies5.add_widget(carousel42)
        movies5.add_widget(carousel43)
        movies5.add_widget(carousel44)
        movies5.add_widget(carousel45)

        movieWrapper5.add_widget(category5)
        movieWrapper5.add_widget(movies5)

##################################(   HUGE CAROUSEL NO6   )#############################################

        carousel51 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel52 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel53 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel54 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel55 = Carousel(direction='right', loop="True", anim_type="linear")

        count6 = 5

        for i in range(count6):
            src = "6" + str(i) + ".jpg"
            image6 = AsyncImage(source=src, allow_stretch=True)
            carousel51.add_widget(image6)

        for i in range(count6):
            src = "6" + str(i) + ".jpg"
            image6 = AsyncImage(source=src, allow_stretch=True)
            carousel52.add_widget(image6)

        for i in range(count6):
            src = "6" + str(i) + ".jpg"
            image6 = AsyncImage(source=src, allow_stretch=True)
            carousel53.add_widget(image6)

        for i in range(count6):
            src = "6" + str(i) + ".jpg"
            image6 = AsyncImage(source=src, allow_stretch=True)
            carousel54.add_widget(image6)

        for i in range(count6):
            src = "6" + str(i) + ".jpg"
            image6 = AsyncImage(source=src, allow_stretch=True)
            carousel55.add_widget(image6)

        carousel51.index = 0
        carousel52.index = 1
        carousel53.index = 2
        carousel54.index = 3
        carousel55.index = 4

        movieWrapper6 = BoxLayout(orientation="vertical")

        category6 = Label(text="Action", font_size = "45", bold="True")
        category6.size_hint = (1, 0.2)
        category6.pos_hint = {'right': 0.6}

        movies6 = BoxLayout()

        movies6.add_widget(carousel51)
        movies6.add_widget(carousel52)
        movies6.add_widget(carousel53)
        movies6.add_widget(carousel54)
        movies6.add_widget(carousel55)

        movieWrapper6.add_widget(category6)
        movieWrapper6.add_widget(movies6)

##################################(   HUGE CAROUSEL NO7   )#############################################

        carousel61 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel62 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel63 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel64 = Carousel(direction='right', loop="True", anim_type="linear")
        carousel65 = Carousel(direction='right', loop="True", anim_type="linear")

        count7 = 7

        for i in range(count7):
            src = "7" + str(i) + ".jpg"
            image7 = AsyncImage(source=src, allow_stretch=True)
            carousel61.add_widget(image7)

        for i in range(count7):
            src = "7" + str(i) + ".jpg"
            image7 = AsyncImage(source=src, allow_stretch=True)
            carousel62.add_widget(image7)

        for i in range(count7):
            src = "7" + str(i) + ".jpg"
            image7 = AsyncImage(source=src, allow_stretch=True)
            carousel63.add_widget(image7)

        for i in range(count7):
            src = "7" + str(i) + ".jpg"
            image7 = AsyncImage(source=src, allow_stretch=True)
            carousel64.add_widget(image7)

        for i in range(count7):
            src = "7" + str(i) + ".jpg"
            image7 = AsyncImage(source=src, allow_stretch=True)
            carousel65.add_widget(image7)

        carousel61.index = 0
        carousel62.index = 1
        carousel63.index = 2
        carousel64.index = 3
        carousel65.index = 4

        movieWrapper7 = BoxLayout(orientation="vertical")

        category7 = Label(text="SciFi", font_size = "45", bold="True")
        category7.size_hint = (1, 0.2)
        category7.pos_hint = {'right': 0.6}

        movies7 = BoxLayout()

        movies7.add_widget(carousel61)
        movies7.add_widget(carousel62)
        movies7.add_widget(carousel63)
        movies7.add_widget(carousel64)
        movies7.add_widget(carousel65)

        movieWrapper7.add_widget(category7)
        movieWrapper7.add_widget(movies7)

############################################################################################

        currentMovie = Label()
        currentMovie.font_size=70
        currentMovie.size_hint=(1,1)
        currentMovie.bold=True
        currentMovie.text = movieName((carousel03.current_slide.source).split(".")[0])

        description = Label()
        description.font_size=35
        description.text_size=(900,300)
        description.valign="top"
        description.italic=True
        description.text = movieDescription((carousel03.current_slide.source).split(".")[0])


        movieInfo.add_widget(currentMovie)
        movieInfo.add_widget(description)






        hugeCarousel = Carousel(direction="bottom", loop="True")
        hugeCarousel.add_widget(movieWrapper1)
        hugeCarousel.add_widget(movieWrapper2)
        hugeCarousel.add_widget(movieWrapper3)
        hugeCarousel.add_widget(movieWrapper4)
        hugeCarousel.add_widget(movieWrapper5)
        hugeCarousel.add_widget(movieWrapper6)
        hugeCarousel.add_widget(movieWrapper7)





        moviesAndCategory.add_widget(hugeCarousel)

        wrapper.add_widget(movieInfo)
        wrapper.add_widget(moviesAndCategory)

        self.add_widget(wrapper)


player = Video(state='pause',
                         options={'allow_stretch': True})


def _load_annotations(self):
    if not self.container:
        return
    self._annotations_labels = []
    annotations = self.annotations
    if not annotations:
        filename = self.source.rsplit('.', 1)
        annotations = filename[0] + '.jsa'
    if exists(annotations):
        with open(annotations, 'r') as fd:
            self._annotations = load(fd)
    if self._annotations:
        for ann in self._annotations:
            self._annotations_labels.append(
                VideoPlayerAnnotation(annotation=ann))

annotation = VideoPlayerAnnotation()



class ScreenVideo(Screen):

    def __init__(self, **kwargs):
        super().__init__()


        self.add_widget(player)
        self.add_widget(annotation)

sm = ScreenManager(transition=FadeTransition(duration=0.1))
screens = [ (ScreenMenu()) , (ScreenVideo()) ]
sm.switch_to(screens[1])
sm.switch_to(screens[0])
sm.screens[1].name = "menu"
sm.screens[0].name = "video"
sm.current="menu"


def change(self):
    print(hugeCarousel.index)
    print(sm.current)
    if(sm.current == "menu"):
        if hugeCarousel.index == 6:
            player.source = loadMovie((carousel63.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 0:
            player.source = loadMovie((carousel03.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 1:
            player.source = loadMovie((carousel13.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 2:
            player.source = loadMovie((carousel23.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 3:
            player.source = loadMovie((carousel33.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 4:
            player.source = loadMovie((carousel43.current_slide.source).split(".")[0])

        elif hugeCarousel.index == 5:
            player.source = loadMovie((carousel53.current_slide.source).split(".")[0])
        player.state="stop"
        player.state= "play"
        time.sleep(0)
        sm.current = "video"
    else:
        if(player.state=="play"):
            player.state = "pause"
        else:
            player.state = "play"

def backMenu(self):
    player.state="stop"
    sm.current="menu"

class MyApp(App):

    def build(self):
        return sm

    def nextSlide(instance):
        if (sm.current == "menu"):

            if hugeCarousel.index == 0:
                description.text = movieDescription((carousel03.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel03.next_slide.source).split(".")[0])
                carousel01.load_next()
                carousel02.load_next()
                carousel03.load_next()
                carousel04.load_next()
                carousel05.load_next()

            elif hugeCarousel.index == 1:
                description.text = movieDescription((carousel13.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel13.next_slide.source).split(".")[0])
                carousel11.load_next()
                carousel12.load_next()
                carousel13.load_next()
                carousel14.load_next()
                carousel15.load_next()

            elif hugeCarousel.index == 2:
                description.text = movieDescription((carousel23.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel23.next_slide.source).split(".")[0])
                carousel21.load_next()
                carousel22.load_next()
                carousel23.load_next()
                carousel24.load_next()
                carousel25.load_next()

            elif hugeCarousel.index == 3:
                description.text = movieDescription((carousel33.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel33.next_slide.source).split(".")[0])
                carousel31.load_next()
                carousel32.load_next()
                carousel33.load_next()
                carousel34.load_next()
                carousel35.load_next()

            elif hugeCarousel.index == 4:
                description.text = movieDescription((carousel43.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel43.next_slide.source).split(".")[0])
                carousel41.load_next()
                carousel42.load_next()
                carousel43.load_next()
                carousel44.load_next()
                carousel45.load_next()

            elif hugeCarousel.index == 5:
                description.text = movieDescription((carousel53.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel53.next_slide.source).split(".")[0])
                carousel51.load_next()
                carousel52.load_next()
                carousel53.load_next()
                carousel54.load_next()
                carousel55.load_next()

            elif hugeCarousel.index == 6:
                description.text = movieDescription((carousel63.next_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel63.next_slide.source).split(".")[0])
                carousel61.load_next()
                carousel62.load_next()
                carousel63.load_next()
                carousel64.load_next()
                carousel65.load_next()



    def previousSlide(instance):
        if (sm.current == "menu"):

            if hugeCarousel.index == 0:
                description.text = movieDescription((carousel03.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel03.previous_slide.source).split(".")[0])
                carousel01.load_previous()
                carousel02.load_previous()
                carousel03.load_previous()
                carousel04.load_previous()
                carousel05.load_previous()

            elif hugeCarousel.index == 1:
                description.text = movieDescription((carousel13.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel13.previous_slide.source).split(".")[0])
                carousel11.load_previous()
                carousel12.load_previous()
                carousel13.load_previous()
                carousel14.load_previous()
                carousel15.load_previous()

            elif hugeCarousel.index == 2:
                description.text = movieDescription((carousel23.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel23.previous_slide.source).split(".")[0])
                carousel21.load_previous()
                carousel22.load_previous()
                carousel23.load_previous()
                carousel24.load_previous()
                carousel25.load_previous()

            elif hugeCarousel.index == 3:
                description.text = movieDescription((carousel33.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel33.previous_slide.source).split(".")[0])
                carousel31.load_previous()
                carousel32.load_previous()
                carousel33.load_previous()
                carousel34.load_previous()
                carousel35.load_previous()

            elif hugeCarousel.index == 4:
                description.text = movieDescription((carousel43.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel43.previous_slide.source).split(".")[0])
                carousel41.load_previous()
                carousel42.load_previous()
                carousel43.load_previous()
                carousel44.load_previous()
                carousel45.load_previous()

            elif hugeCarousel.index == 5:
                description.text = movieDescription((carousel53.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel53.previous_slide.source).split(".")[0])
                carousel51.load_previous()
                carousel52.load_previous()
                carousel53.load_previous()
                carousel54.load_previous()
                carousel55.load_previous()

            elif hugeCarousel.index == 6:
                description.text = movieDescription((carousel63.previous_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel63.previous_slide.source).split(".")[0])
                carousel61.load_previous()
                carousel62.load_previous()
                carousel63.load_previous()
                carousel64.load_previous()
                carousel65.load_previous()

    def nextCategory(instance):
        if (sm.current == "menu"):

            hugeCarousel.load_next()

            if hugeCarousel.index == 5:
                description.text = movieDescription((carousel63.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel63.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 6:
                description.text = movieDescription((carousel03.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel03.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 0:
                description.text = movieDescription((carousel13.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel13.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 1:
                description.text = movieDescription((carousel23.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel23.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 2:
                description.text = movieDescription((carousel33.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel33.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 3:
                description.text = movieDescription((carousel43.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel43.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 4:
                description.text = movieDescription((carousel53.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel53.current_slide.source).split(".")[0])


    def previousCategory(instance):
        if (sm.current == "menu"):

            hugeCarousel.load_previous()

            if hugeCarousel.index == 1:
                description.text = movieDescription((carousel03.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel03.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 2:
                description.text = movieDescription((carousel13.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel13.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 3:
                description.text = movieDescription((carousel23.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel23.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 4:
                description.text = movieDescription((carousel33.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel33.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 5:
                description.text = movieDescription((carousel43.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel43.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 6:
                description.text = movieDescription((carousel53.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel53.current_slide.source).split(".")[0])

            elif hugeCarousel.index == 0:
                description.text = movieDescription((carousel63.current_slide.source).split(".")[0])
                currentMovie.text = movieName((carousel63.current_slide.source).split(".")[0])

        pass



    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self.root)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')

        if keycode[1] == "right":
            self.nextSlide()

        if keycode[1] == "left":
            self.previousSlide()

        if keycode[1] == "up":
            self.previousCategory()

        if keycode[1] == "down":
            self.nextCategory()

        if (keycode[1] == "enter"):
            change(sm)

        if keycode[0] == 1073741824:
            backMenu(self)

        if keycode[0] == 1073741942:
            forward()



        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()


if __name__ == "__main__":
    MyApp().run()
