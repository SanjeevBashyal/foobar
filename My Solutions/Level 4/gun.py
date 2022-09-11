#Level 4 Challenge 2 Bringing a Gun to a Trainer Fight
import math as m

def solution(dimensions, your_position, trainer_position, distance):
    geo=Geometry(dimensions)
    least_distance=geo.distance_formula(your_position,trainer_position)
    if least_distance>distance:
        return 0
    check_list=[your_position]
    geo.initialize(tuple(your_position),tuple(trainer_position))
    while check_list:
        all_reflected_my_position=[geo.reflection_mine(my_image,your_position,distance) for my_image in check_list]
        check_list=[item for sublist in all_reflected_my_position for item in sublist]

    trainer_checklist=[trainer_position]
    while trainer_checklist:
        all_reflected_trainer_position=[geo.reflection_trainer(trainer_image,your_position,distance) for trainer_image in trainer_checklist]
        trainer_checklist=[item for sublist in all_reflected_trainer_position for item in sublist]

    return len(geo.trainer_dist)

class Geometry:
    def __init__(self,dimensions):
        self.X=dimensions[0]
        self.Y=dimensions[1]
        self.trainer_images=set()
        self.my_images=set()
        self.my_dist={}
        self.trainer_dist={}

    def initialize(self,my_position,trainer_position):
        self.my_images.add(my_position)
        self.trainer_images.add(trainer_position)
        bearing=self.calculate_bearing(my_position,trainer_position)
        distance=self.distance_formula(my_position,trainer_position)
        self.trainer_dist[bearing]=distance

    def reflection_about_Y(self,xy,offset=0):
        x,y=xy
        return (x,2*offset-y)

    def reflection_about_X(self,xy,offset=0):
        x,y=xy
        return (2*offset-x,y)

    def reflection_from_walls(self,xy):
        return [self.reflection_about_Y(xy,0),self.reflection_about_Y(xy,self.Y),self.reflection_about_X(xy,0),self.reflection_about_X(xy,self.X)]

    def reflection_mine(self,my_image,my_orginal_position,distance):
            my_reflections=self.reflection_from_walls(my_image)
            out=[]
            for i in range(4):
                if my_reflections[i] in self.my_images:
                    continue
                else:
                    bearing=self.calculate_bearing(my_orginal_position,my_reflections[i])
                    if bearing in self.my_dist:
                        continue
                    else:
                        distance_between_me_and_my_image=self.distance_formula(my_orginal_position,my_reflections[i])
                        if distance_between_me_and_my_image>distance:
                            continue
                        else:
                            self.my_dist[bearing]=distance_between_me_and_my_image
                            out.append(my_reflections[i])
                            self.my_images.add(my_reflections[i])
            return out

    def reflection_trainer(self,trainer_image,my_orginal_position,distance):
            trainer_reflections=self.reflection_from_walls(trainer_image)
            out=[]
            for i in range(4):
                if trainer_reflections[i] in self.trainer_images:
                    continue
                else:
                    bearing=self.calculate_bearing(my_orginal_position,trainer_reflections[i])
                    if bearing in self.trainer_dist:
                        continue
                    else:
                        distance_between_me_and_trainer_image=self.distance_formula(my_orginal_position,trainer_reflections[i])
                        if distance_between_me_and_trainer_image>distance:
                            continue
                        else:
                            if bearing in self.my_dist:
                                if distance_between_me_and_trainer_image>self.my_dist[bearing]:
                                    continue                                    
                            self.trainer_dist[bearing]=distance_between_me_and_trainer_image
                            out.append(trainer_reflections[i])
                            self.trainer_images.add(trainer_reflections[i])
            return out


    def distance_formula(self,xy1,xy2):
        return m.sqrt((xy2[0]-xy1[0])**2+(xy2[1]-xy1[1])**2)

    def distance_formula_multiple(self,xy1,xys):
        return [self.distance_formula(xy1,xy) for xy in xys]
    
    def calculate_bearing(self,xy1,xy2):
        return (360+m.degrees(m.atan2(xy2[1]-xy1[1],xy2[0]-xy1[0])))%360

    def calculate_bearings(self,xy1,xys):
        return [self.calculate_bearing(xy1,xy) for xy in xys]


# print(solution([300,275], [150,150], [185,100], 500))
# print(solution([5,5], [1,1], [1,4], 20))
# print(solution([4,5], [1,2], [2,3], 50))
# print(solution([3,2], [1,1], [2,1], 4))

# print(solution([23,10], [6,4], [3,2], 23))
# print(solution([10,10], [4,4], [3,3], 5000))

