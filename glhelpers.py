import pyglet.gl

def glfloat_list(list):
    return (pyglet.gl.GLfloat * len(list))(*list)

