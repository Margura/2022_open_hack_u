PITCH0 = ["C", "D", "E", "F", "G", "A", "B"]
PITCH1 = ["1", "2", "3", "4", "5"]

def h_img2melody_li(v_img) :
    pitch_li = []
    for v in v_img :
        index0 = v % 7
        index1 = v // 100 + 2
        pitch_li.append(PITCH0[index0] + PITCH1[index1])
    return pitch_li
        
def s_img2base_li(v_img) :
    pitch_li = []
    for v in v_img :
        index0 = v % 7
        index1 = v // 100
        pitch_li.append(PITCH0[index0] + PITCH1[index1])
    return pitch_li

def v_img2len_li(v_img) :
    len_li = []
    ratio = 2/255
    for v in v_img :
        len_li.append(v * ratio)
    return len_li