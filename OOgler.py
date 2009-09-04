"""
This is the main module for launching the OOgler
"""
import scene.root

if __name__ == '__main__':
    root = scene.root.SceneRoot()
    root.main_loop()

