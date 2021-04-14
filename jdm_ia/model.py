def predict(model_name):
    import os

    ROOT_DIR = os.path.abspath(os.getcwd())
    model_path = os.path.join(ROOT_DIR, "models", model_name)

    print('ROOT_DIR:      ', ROOT_DIR)
    print('model_path:    ', model_path)

    with open(model_path) as f:
        return f.read()