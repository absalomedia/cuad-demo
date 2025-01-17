from v2_backend.dataset_processor import generate_dataset
from v2_backend.model import Model

# generate the dataset
#generate_dataset('dataset', 10)

# build the model
m = Model(padding=256)
m.build_model()
print(m.model.summary())

m.train('dataset/train.pkl', 3)
m.save_model('models/v1')
