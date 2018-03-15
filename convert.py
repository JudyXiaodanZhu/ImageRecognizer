import coremltools
output_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
scale = 1/255.
coreml_model = coremltools.converters.keras.convert('./classify_app', input_names='image', image_input_names='image',
                                                    output_names='output', class_labels=output_labels,
                                                    image_scale=scale)
coreml_model.author = 'Judy Zhu'
coreml_model.license = 'UofT'
coreml_model.short_description = 'Model to classify pictures'
coreml_model.input_description['image'] = 'Real pictures of 10 different classes.'
coreml_model.output_description['output'] = 'Results'

coreml_model.save('PhotoClassifier.mlmodel')