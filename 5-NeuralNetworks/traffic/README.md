Accuracy after 10th epoch:
    x1 Conv2D (relu, 32 filters), x1 MaxPooling2D layers: 0.0557

    x2 Conv2D (relu, 32 filters, 3x3), x2 MaxPooling2D layers: 0.8958
    x2 Conv2D (sigmoid, 32 filters, 3x3), x2 MaxPooling2D layers: 0.6033

    x2 Conv2D (relu, 32 filters), x2 MaxPooling2D layers, x1 Dense (256 units): 0.9427
    x2 Conv2D (relu, 16 filters), x2 MaxPooling2D layers, x1 Dense (128 units): 0.9260
    x2 Conv2D (relu, 16 filters), x2 MaxPooling2D layers, x1 Dense (64 units): 0.8166

    x2 Conv2D (relu, 32 filters, 4x4), x2 MaxPooling2D layers: 0.8723
    x2 Conv2D (relu, 32 filters, 2x2), x2 MaxPooling2D layers: 0.9018

    x2 Conv2D (relu, 32 filters, 3x3), x2 MaxPooling2D (3x3) layers: 0.5912
    x2 Conv2D (relu, 32 filters, 3x3), x2 AveragePooling2D (2x2) layers: 0.9714

    x2 Conv2D (relu, 32 filters, 3x3), x2 AveragePooling2D (2x2) layers, x1 Dropout (0.3): 0.981
    x2 Conv2D (relu, 32 filters, 3x3), x2 AveragePooling2D (2x2) layers, x1 Dropout (0.7): 0.9675

    x2 Conv2D (relu, 48 filters, 2x2), x2 MaxPooling2D layers, x1 Dense (256 units): 0.9782
    x2 Conv2D (relu, 48 filters, 2x2), x2 MaxPooling2D layers, x1 Dense (256 units), x1 Dropout (0.3): 0.9792

    x2 Conv2D (relu, 32 filters, 3x3), x2 AveragePooling2D (2x2) layers, x2 Dense (128 units): 0.9634

- More Conv and Pooling layers gives better accuracy
- Average pooling gives better accuracy than max pooling
- Less dropout gives better accuracy, but there is a bigger chance of overfitting
- More filters gives better accuracy
- More dense units gives better accuracy
- Bigger pooling size gives worse accuracy