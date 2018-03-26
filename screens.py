from vidpy import Clip, Composition

clips = []
# clipsAll = [clips,
for i in range(0,3):
    clip = Clip('jobs_640_480_1.mp4', offset=i*0.5, start=0.3, end=6)
    clips.append(clip)

for i in range(0,3):
    clip2 = Clip('sheliak_636_480_1.mp4', offset=i*2, start=1.87, end=2.9)
    clips.append(clip2)

# picard
# for i in range(0):
#     clip26 = Clip('sheliak_636_480_1.mp4', offset=i*.4, start=2.9, end=3)
#     clips.append(clip26)
# for i in range(0):
#     clip3 = Clip('sheliak_636_480_p.mp4', start=7, end=7.5)
#     clips.append(clip3)

# for i in range(0):
#     clip6 = Clip('sheliak_636_480_p.mp4', offset=7.4, start=0, end=1)
#     clips.append(clip6)
# alien
for i in range(0,4):
    clip7 = Clip('sheliak_636_480_a.mp4', offset=4.2+(i*2), start=.9, end=2)
    clips.append(clip7)
# for i in range(0,3):
#     clip5 = Clip('holodeck_b.mp4', offset=8.5+(i*2), start=0, end=0.5)
#     clips.append(clip5)
# for i in range(0,3):
#     clip13 = Clip('jobs_640_480_1.mp4', offset=i*0.5, start=10, end=11)
#     clips.append(clip13)
for i in range(0,5):
    clip8 = Clip('holodeck_b.mp4', offset=7.5+(i*.3), start=1, end=5)
    clips.append(clip8)

for i in range(0,5):
    clip9 = Clip('holodeck_b.mp4', offset=14.5+(i*0.2), start=8, end=10)
    clips.append(clip9)
    clip28 = Clip('woods2.mp4', offset=7+(i*.2), start=0, end=.75)
    clips.append(clip28)

# for i in range(0,6):
#     clip10 = Clip('sheliak_636_480_a.mp4', offset=8.5+(i*.3), start=1, end=1.2)
#     clips.append(clip10)
# for i in range(0,2):
#     clip11 = Clip('jobs_640_480_4.mp4', offset=8.85+(i*0.3), start=1, end=2)
#     clips.append(clip11)
# for i in range(0,3):
#     clip12 = Clip('jobs_640_480_1.mp4', offset=9+i*0.3, start=1, end=2)
#     clips.append(clip12)
#     # steve jobs_640_480_1


for i in range(0,3):
    # clip29 = Clip('lotr_reading.mp4', offset=16+(i*0.5), start=1.0, end=1.6)
    # clips.append(clip29)
    # bold and shy
    clip15 = Clip('woods1.mp4', offset=15.2+(i*.2), start=0, end=.6)
    clips.append(clip15)
    # dancing
    clip14 = Clip('woods1.mp4', offset=17+(i*.2), start=0, end=1)
    clips.append(clip14)
    # clip27 = Clip('lotr_reading.mp4', offset=18.3+(i*0.2), start=9.5, end=11.5)
    # clips.append(clip27)

    clip16 = Clip('woods1.mp4', offset=20+(i*.6), start=0, end=.9)
    clips.append(clip16)
# clip23 = Clip('woods3.mp4', offset=16, start=0, end=0.5)
# clips.append(clip23)
# clip17 = Clip('lotr.mp4', offset=15, start=4, end=5)
# clips.append(clip17)

# clip18 = Clip('lotr.mp4', offset=15.5, start=8, end=9)
# clips.append(clip18)

# clip24 = Clip('woods2.mp4', offset=15, start=0, end=.4)
# clips.append(clip24)

# reading
for i in range(0,3):
    clip19 = Clip('lotr_reading.mp4', offset=10.9+(i*0.5), start=1, end=8.8)
    clips.append(clip19)
for i in range(0,5):
    clip25 = Clip('holodeck_b.mp4', offset=12.5+(i*0.3), start=12, end=13)
    clips.append(clip25)
# //late
# for i in range(0,5):
#     clip19 = Clip('lotr_late2.mp4', offset=15.6+(i*0.4), start=1, end=6)
#     clips.append(clip19)



for i in range(0,3):
    clip20 = Clip('lotr_late2.mp4', offset=16.4+(i*0.7), start=0, end=7)
    clips.append(clip20)

for i in range(0,7):
    clip29 = Clip('holodeck_b.mp4', offset=18.5+(i*0.2), start=18, end=20)
    clips.append(clip29)

for i in range(0,3):
    clip21 = Clip('jobs_640_480_1.mp4', offset=19.4+i*0.5, start=0.3, end=6)
    clips.append(clip21)

for i in range(0,3):
    clip22 = Clip('sheliak_636_480_1.mp4', offset=19.3+i*2, start=1.87, end=2.9)
    clips.append(clip22)


# clip4 = Clip('sheliak_636_480_1.mp4', offset=8, start=1.87, end=2.9)
# clips.append(clip4)

comp = Composition(clips)
# comp = Composition(clips, singletrack=True)

# comp.preview()
comp.save('screens_doors_men_alienmen_mix.mp4')
