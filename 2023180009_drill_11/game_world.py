world = [[] for _ in range(4)]
collision_paris = {}    #{key: [[], []]} 리스트 오브 리스트로 들어있다.

def add_collision_pair(group, a, b):
    #key : group(boy, ball, grass등등 충돌하는 대상을 알려주는 문자열)
    if group not in collision_paris:
        collision_paris[group] = [ [], [] ]     #초기화 해준다.
    if a:           #a가 있으면
        collision_paris[group][0].append(a)
    if b:           #b가 있으면
        collision_paris[group][1].append(b)

#def remove_object()에서 추가
def remove_collision_object(o):
    for pairs in collision_paris.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def add_object(o, depth = 0):
    world[depth].append(o)
#하나만 넣음

def add_objects(ol, depth = 0):
    world[depth] += ol
#여러개 넣음

def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)             #월드에서 날리고
            remove_collision_object(o)  #충돌처리에서도 없애고
            del o                       #메모리에서도 완전히 날려줌
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in world:
        layer.clear()



# fill here
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def handle_collisions():
    for group, paris in collision_paris.items():
        for a in paris[0]:
            for b in paris[1]:
                if collide(a, b):  #만약 a,b 가 충돌이 되었다면?
                    #서로에게 서로를 알려준다. 무엇과 충돌했는지
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)