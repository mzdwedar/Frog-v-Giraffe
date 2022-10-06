from utils.dataset import build_dataset
from utils.model import model_builder, save_model
from utils.data_pipeline import get_train_gen, get_valid_gen



if __name__ == "__main__":
    print("building dataset: ---------------------------------------------------------------")
    
    build_dataset()
    
    print("building the model: ---------------------------------------------------------------")
    model = model_builder()

    print("build data pipeline: ---------------------------------------------------------------")
    train_generator = get_train_gen()
    valid_generator = get_valid_gen()

    print("start training: --------------------------------------------------------------------")
    history = model.fit(train_generator, validation_data=valid_generator, epochs= 10, verbose=1)
    
    print("saving model: -------------------------------------------------------------------")
    save_model(model, 'frog_v_giraffe', history)
