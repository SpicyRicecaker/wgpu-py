"""Mappings for the wgpu-native backend."""

# THIS CODE IS AUTOGENERATED - DO NOT EDIT


# There are 255 enum mappings

enummap = {
    "AddressMode.clamp-to-edge": 1,
    "AddressMode.mirror-repeat": 3,
    "AddressMode.repeat": 2,
    "BlendFactor.constant": 12,
    "BlendFactor.dst": 7,
    "BlendFactor.dst-alpha": 9,
    "BlendFactor.one": 2,
    "BlendFactor.one-minus-constant": 13,
    "BlendFactor.one-minus-dst": 8,
    "BlendFactor.one-minus-dst-alpha": 10,
    "BlendFactor.one-minus-src": 4,
    "BlendFactor.one-minus-src-alpha": 6,
    "BlendFactor.one-minus-src1": 15,
    "BlendFactor.one-minus-src1-alpha": 17,
    "BlendFactor.src": 3,
    "BlendFactor.src-alpha": 5,
    "BlendFactor.src-alpha-saturated": 11,
    "BlendFactor.src1": 14,
    "BlendFactor.src1-alpha": 16,
    "BlendFactor.zero": 1,
    "BlendOperation.add": 1,
    "BlendOperation.max": 5,
    "BlendOperation.min": 4,
    "BlendOperation.reverse-subtract": 3,
    "BlendOperation.subtract": 2,
    "BufferBindingType.read-only-storage": 4,
    "BufferBindingType.storage": 3,
    "BufferBindingType.uniform": 2,
    "BufferMapState.mapped": 3,
    "BufferMapState.pending": 2,
    "BufferMapState.unmapped": 1,
    "CompareFunction.always": 8,
    "CompareFunction.equal": 3,
    "CompareFunction.greater": 5,
    "CompareFunction.greater-equal": 7,
    "CompareFunction.less": 2,
    "CompareFunction.less-equal": 4,
    "CompareFunction.never": 1,
    "CompareFunction.not-equal": 6,
    "CompilationMessageType.error": 1,
    "CompilationMessageType.info": 3,
    "CompilationMessageType.warning": 2,
    "CullMode.back": 3,
    "CullMode.front": 2,
    "CullMode.none": 1,
    "DeviceLostReason.destroyed": 2,
    "DeviceLostReason.unknown": 1,
    "ErrorFilter.internal": 3,
    "ErrorFilter.out-of-memory": 2,
    "ErrorFilter.validation": 1,
    "FeatureName.bgra8unorm-storage": 12,
    "FeatureName.clip-distances": 15,
    "FeatureName.depth-clip-control": 1,
    "FeatureName.depth32float-stencil8": 2,
    "FeatureName.dual-source-blending": 16,
    "FeatureName.float32-blendable": 14,
    "FeatureName.float32-filterable": 13,
    "FeatureName.indirect-first-instance": 9,
    "FeatureName.rg11b10ufloat-renderable": 11,
    "FeatureName.shader-f16": 10,
    "FeatureName.texture-compression-astc": 7,
    "FeatureName.texture-compression-astc-sliced-3d": 8,
    "FeatureName.texture-compression-bc": 4,
    "FeatureName.texture-compression-bc-sliced-3d": 5,
    "FeatureName.texture-compression-etc2": 6,
    "FeatureName.timestamp-query": 3,
    "FilterMode.linear": 2,
    "FilterMode.nearest": 1,
    "FrontFace.ccw": 1,
    "FrontFace.cw": 2,
    "IndexFormat.uint16": 1,
    "IndexFormat.uint32": 2,
    "LoadOp.clear": 2,
    "LoadOp.load": 1,
    "MipmapFilterMode.linear": 2,
    "MipmapFilterMode.nearest": 1,
    "PowerPreference.high-performance": 2,
    "PowerPreference.low-power": 1,
    "PrimitiveTopology.line-list": 2,
    "PrimitiveTopology.line-strip": 3,
    "PrimitiveTopology.point-list": 1,
    "PrimitiveTopology.triangle-list": 4,
    "PrimitiveTopology.triangle-strip": 5,
    "QueryType.occlusion": 1,
    "QueryType.timestamp": 2,
    "SamplerBindingType.comparison": 4,
    "SamplerBindingType.filtering": 2,
    "SamplerBindingType.non-filtering": 3,
    "StencilOperation.decrement-clamp": 6,
    "StencilOperation.decrement-wrap": 8,
    "StencilOperation.increment-clamp": 5,
    "StencilOperation.increment-wrap": 7,
    "StencilOperation.invert": 4,
    "StencilOperation.keep": 1,
    "StencilOperation.replace": 3,
    "StencilOperation.zero": 2,
    "StorageTextureAccess.read-only": 3,
    "StorageTextureAccess.read-write": 4,
    "StorageTextureAccess.write-only": 2,
    "StoreOp.discard": 2,
    "StoreOp.store": 1,
    "TextureAspect.all": 1,
    "TextureAspect.depth-only": 3,
    "TextureAspect.stencil-only": 2,
    "TextureDimension.1d": 1,
    "TextureDimension.2d": 2,
    "TextureDimension.3d": 3,
    "TextureFormat.astc-10x10-unorm": 90,
    "TextureFormat.astc-10x10-unorm-srgb": 91,
    "TextureFormat.astc-10x5-unorm": 84,
    "TextureFormat.astc-10x5-unorm-srgb": 85,
    "TextureFormat.astc-10x6-unorm": 86,
    "TextureFormat.astc-10x6-unorm-srgb": 87,
    "TextureFormat.astc-10x8-unorm": 88,
    "TextureFormat.astc-10x8-unorm-srgb": 89,
    "TextureFormat.astc-12x10-unorm": 92,
    "TextureFormat.astc-12x10-unorm-srgb": 93,
    "TextureFormat.astc-12x12-unorm": 94,
    "TextureFormat.astc-12x12-unorm-srgb": 95,
    "TextureFormat.astc-4x4-unorm": 68,
    "TextureFormat.astc-4x4-unorm-srgb": 69,
    "TextureFormat.astc-5x4-unorm": 70,
    "TextureFormat.astc-5x4-unorm-srgb": 71,
    "TextureFormat.astc-5x5-unorm": 72,
    "TextureFormat.astc-5x5-unorm-srgb": 73,
    "TextureFormat.astc-6x5-unorm": 74,
    "TextureFormat.astc-6x5-unorm-srgb": 75,
    "TextureFormat.astc-6x6-unorm": 76,
    "TextureFormat.astc-6x6-unorm-srgb": 77,
    "TextureFormat.astc-8x5-unorm": 78,
    "TextureFormat.astc-8x5-unorm-srgb": 79,
    "TextureFormat.astc-8x6-unorm": 80,
    "TextureFormat.astc-8x6-unorm-srgb": 81,
    "TextureFormat.astc-8x8-unorm": 82,
    "TextureFormat.astc-8x8-unorm-srgb": 83,
    "TextureFormat.bc1-rgba-unorm": 44,
    "TextureFormat.bc1-rgba-unorm-srgb": 45,
    "TextureFormat.bc2-rgba-unorm": 46,
    "TextureFormat.bc2-rgba-unorm-srgb": 47,
    "TextureFormat.bc3-rgba-unorm": 48,
    "TextureFormat.bc3-rgba-unorm-srgb": 49,
    "TextureFormat.bc4-r-snorm": 51,
    "TextureFormat.bc4-r-unorm": 50,
    "TextureFormat.bc5-rg-snorm": 53,
    "TextureFormat.bc5-rg-unorm": 52,
    "TextureFormat.bc6h-rgb-float": 55,
    "TextureFormat.bc6h-rgb-ufloat": 54,
    "TextureFormat.bc7-rgba-unorm": 56,
    "TextureFormat.bc7-rgba-unorm-srgb": 57,
    "TextureFormat.bgra8unorm": 23,
    "TextureFormat.bgra8unorm-srgb": 24,
    "TextureFormat.depth16unorm": 39,
    "TextureFormat.depth24plus": 40,
    "TextureFormat.depth24plus-stencil8": 41,
    "TextureFormat.depth32float": 42,
    "TextureFormat.depth32float-stencil8": 43,
    "TextureFormat.eac-r11snorm": 65,
    "TextureFormat.eac-r11unorm": 64,
    "TextureFormat.eac-rg11snorm": 67,
    "TextureFormat.eac-rg11unorm": 66,
    "TextureFormat.etc2-rgb8a1unorm": 60,
    "TextureFormat.etc2-rgb8a1unorm-srgb": 61,
    "TextureFormat.etc2-rgb8unorm": 58,
    "TextureFormat.etc2-rgb8unorm-srgb": 59,
    "TextureFormat.etc2-rgba8unorm": 62,
    "TextureFormat.etc2-rgba8unorm-srgb": 63,
    "TextureFormat.r16float": 7,
    "TextureFormat.r16sint": 6,
    "TextureFormat.r16uint": 5,
    "TextureFormat.r32float": 12,
    "TextureFormat.r32sint": 14,
    "TextureFormat.r32uint": 13,
    "TextureFormat.r8sint": 4,
    "TextureFormat.r8snorm": 2,
    "TextureFormat.r8uint": 3,
    "TextureFormat.r8unorm": 1,
    "TextureFormat.rg11b10ufloat": 27,
    "TextureFormat.rg16float": 17,
    "TextureFormat.rg16sint": 16,
    "TextureFormat.rg16uint": 15,
    "TextureFormat.rg32float": 29,
    "TextureFormat.rg32sint": 31,
    "TextureFormat.rg32uint": 30,
    "TextureFormat.rg8sint": 11,
    "TextureFormat.rg8snorm": 9,
    "TextureFormat.rg8uint": 10,
    "TextureFormat.rg8unorm": 8,
    "TextureFormat.rgb10a2uint": 25,
    "TextureFormat.rgb10a2unorm": 26,
    "TextureFormat.rgb9e5ufloat": 28,
    "TextureFormat.rgba16float": 34,
    "TextureFormat.rgba16sint": 33,
    "TextureFormat.rgba16uint": 32,
    "TextureFormat.rgba32float": 35,
    "TextureFormat.rgba32sint": 37,
    "TextureFormat.rgba32uint": 36,
    "TextureFormat.rgba8sint": 22,
    "TextureFormat.rgba8snorm": 20,
    "TextureFormat.rgba8uint": 21,
    "TextureFormat.rgba8unorm": 18,
    "TextureFormat.rgba8unorm-srgb": 19,
    "TextureFormat.stencil8": 38,
    "TextureSampleType.depth": 4,
    "TextureSampleType.float": 2,
    "TextureSampleType.sint": 5,
    "TextureSampleType.uint": 6,
    "TextureSampleType.unfilterable-float": 3,
    "TextureViewDimension.1d": 1,
    "TextureViewDimension.2d": 2,
    "TextureViewDimension.2d-array": 3,
    "TextureViewDimension.3d": 6,
    "TextureViewDimension.cube": 4,
    "TextureViewDimension.cube-array": 5,
    "VertexFormat.float16": 25,
    "VertexFormat.float16x2": 26,
    "VertexFormat.float16x4": 27,
    "VertexFormat.float32": 28,
    "VertexFormat.float32x2": 29,
    "VertexFormat.float32x3": 30,
    "VertexFormat.float32x4": 31,
    "VertexFormat.sint16": 16,
    "VertexFormat.sint16x2": 17,
    "VertexFormat.sint16x4": 18,
    "VertexFormat.sint32": 36,
    "VertexFormat.sint32x2": 37,
    "VertexFormat.sint32x3": 38,
    "VertexFormat.sint32x4": 39,
    "VertexFormat.sint8": 4,
    "VertexFormat.sint8x2": 5,
    "VertexFormat.sint8x4": 6,
    "VertexFormat.snorm16": 22,
    "VertexFormat.snorm16x2": 23,
    "VertexFormat.snorm16x4": 24,
    "VertexFormat.snorm8": 10,
    "VertexFormat.snorm8x2": 11,
    "VertexFormat.snorm8x4": 12,
    "VertexFormat.uint16": 13,
    "VertexFormat.uint16x2": 14,
    "VertexFormat.uint16x4": 15,
    "VertexFormat.uint32": 32,
    "VertexFormat.uint32x2": 33,
    "VertexFormat.uint32x3": 34,
    "VertexFormat.uint32x4": 35,
    "VertexFormat.uint8": 1,
    "VertexFormat.uint8x2": 2,
    "VertexFormat.uint8x4": 3,
    "VertexFormat.unorm16": 19,
    "VertexFormat.unorm16x2": 20,
    "VertexFormat.unorm16x4": 21,
    "VertexFormat.unorm8": 7,
    "VertexFormat.unorm8x2": 8,
    "VertexFormat.unorm8x4": 9,
    "VertexFormat.unorm8x4-bgra": 41,
    "VertexStepMode.instance": 3,
    "VertexStepMode.vertex": 2,
}

# There are 47 struct-field enum mappings

cstructfield2enum = {
    "BlendComponent.dstFactor": "BlendFactor",
    "BlendComponent.operation": "BlendOperation",
    "BlendComponent.srcFactor": "BlendFactor",
    "BufferBindingLayout.type": "BufferBindingType",
    "ColorTargetState.format": "TextureFormat",
    "CompilationMessage.type": "CompilationMessageType",
    "DepthStencilState.depthCompare": "CompareFunction",
    "DepthStencilState.format": "TextureFormat",
    "PrimitiveState.cullMode": "CullMode",
    "PrimitiveState.frontFace": "FrontFace",
    "PrimitiveState.stripIndexFormat": "IndexFormat",
    "PrimitiveState.topology": "PrimitiveTopology",
    "QuerySetDescriptor.type": "QueryType",
    "RenderBundleEncoderDescriptor.depthStencilFormat": "TextureFormat",
    "RenderPassColorAttachment.loadOp": "LoadOp",
    "RenderPassColorAttachment.storeOp": "StoreOp",
    "RenderPassDepthStencilAttachment.depthLoadOp": "LoadOp",
    "RenderPassDepthStencilAttachment.depthStoreOp": "StoreOp",
    "RenderPassDepthStencilAttachment.stencilLoadOp": "LoadOp",
    "RenderPassDepthStencilAttachment.stencilStoreOp": "StoreOp",
    "RequestAdapterOptions.powerPreference": "PowerPreference",
    "SamplerBindingLayout.type": "SamplerBindingType",
    "SamplerDescriptor.addressModeU": "AddressMode",
    "SamplerDescriptor.addressModeV": "AddressMode",
    "SamplerDescriptor.addressModeW": "AddressMode",
    "SamplerDescriptor.compare": "CompareFunction",
    "SamplerDescriptor.magFilter": "FilterMode",
    "SamplerDescriptor.minFilter": "FilterMode",
    "SamplerDescriptor.mipmapFilter": "MipmapFilterMode",
    "StencilFaceState.compare": "CompareFunction",
    "StencilFaceState.depthFailOp": "StencilOperation",
    "StencilFaceState.failOp": "StencilOperation",
    "StencilFaceState.passOp": "StencilOperation",
    "StorageTextureBindingLayout.access": "StorageTextureAccess",
    "StorageTextureBindingLayout.format": "TextureFormat",
    "StorageTextureBindingLayout.viewDimension": "TextureViewDimension",
    "SurfaceConfiguration.format": "TextureFormat",
    "TexelCopyTextureInfo.aspect": "TextureAspect",
    "TextureBindingLayout.sampleType": "TextureSampleType",
    "TextureBindingLayout.viewDimension": "TextureViewDimension",
    "TextureDescriptor.dimension": "TextureDimension",
    "TextureDescriptor.format": "TextureFormat",
    "TextureViewDescriptor.aspect": "TextureAspect",
    "TextureViewDescriptor.dimension": "TextureViewDimension",
    "TextureViewDescriptor.format": "TextureFormat",
    "VertexAttribute.format": "VertexFormat",
    "VertexBufferLayout.stepMode": "VertexStepMode",
}

enum_str2int = {
    "BackendType": {
        "Undefined": 0,
        "Null": 1,
        "WebGPU": 2,
        "D3D11": 3,
        "D3D12": 4,
        "Metal": 5,
        "Vulkan": 6,
        "OpenGL": 7,
        "OpenGLES": 8,
    },
    "NativeFeature": {
        "push-constants": 196609,
        "texture-adapter-specific-format-features": 196610,
        "multi-draw-indirect": 196611,
        "multi-draw-indirect-count": 196612,
        "vertex-writable-storage": 196613,
        "texture-binding-array": 196614,
        "sampled-texture-and-storage-buffer-array-non-uniform-indexing": 196615,
        "pipeline-statistics-query": 196616,
        "storage-resource-binding-array": 196617,
        "partially-bound-binding-array": 196618,
        "texture-format16bit-norm": 196619,
        "texture-compression-astc-hdr": 196620,
        "mappable-primary-buffers": 196622,
        "buffer-binding-array": 196623,
        "uniform-buffer-and-storage-texture-array-non-uniform-indexing": 196624,
        "spirv-shader-passthrough": 196631,
        "vertex-attribute64bit": 196633,
        "texture-format-nv12": 196634,
        "ray-tracing-acceleration-structure": 196635,
        "ray-query": 196636,
        "shader-f64": 196637,
        "shader-i16": 196638,
        "shader-primitive-index": 196639,
        "shader-early-depth-test": 196640,
        "subgroup": 196641,
        "subgroup-vertex": 196642,
        "subgroup-barrier": 196643,
        "timestamp-query-inside-encoders": 196644,
        "timestamp-query-inside-passes": 196645,
    },
    "PipelineStatisticName": {
        "vertex-shader-invocations": 0,
        "clipper-invocations": 1,
        "clipper-primitives-out": 2,
        "fragment-shader-invocations": 3,
        "compute-shader-invocations": 4,
    },
    "Dx12Compiler": {
        "Undefined": 0,
        "Fxc": 1,
        "Dxc": 2,
    },
}

enum_int2str = {
    "BackendType": {
        0: "Undefined",
        1: "Null",
        2: "WebGPU",
        3: "D3D11",
        4: "D3D12",
        5: "Metal",
        6: "Vulkan",
        7: "OpenGL",
        8: "OpenGLES",
    },
    "AdapterType": {
        1: "DiscreteGPU",
        2: "IntegratedGPU",
        3: "CPU",
        4: "Unknown",
    },
    "ErrorType": {
        1: "NoError",
        2: "Validation",
        3: "OutOfMemory",
        4: "Internal",
        5: "Unknown",
    },
    "DeviceLostReason": {
        1: "unknown",
        2: "destroyed",
        3: "InstanceDropped",
        4: "FailedCreation",
    },
    "TextureFormat": {
        0: "Undefined",
        1: "r8unorm",
        2: "r8snorm",
        3: "r8uint",
        4: "r8sint",
        5: "r16uint",
        6: "r16sint",
        7: "r16float",
        8: "rg8unorm",
        9: "rg8snorm",
        10: "rg8uint",
        11: "rg8sint",
        12: "r32float",
        13: "r32uint",
        14: "r32sint",
        15: "rg16uint",
        16: "rg16sint",
        17: "rg16float",
        18: "rgba8unorm",
        19: "rgba8unorm-srgb",
        20: "rgba8snorm",
        21: "rgba8uint",
        22: "rgba8sint",
        23: "bgra8unorm",
        24: "bgra8unorm-srgb",
        25: "rgb10a2uint",
        26: "rgb10a2unorm",
        27: "rg11b10ufloat",
        28: "rgb9e5ufloat",
        29: "rg32float",
        30: "rg32uint",
        31: "rg32sint",
        32: "rgba16uint",
        33: "rgba16sint",
        34: "rgba16float",
        35: "rgba32float",
        36: "rgba32uint",
        37: "rgba32sint",
        38: "stencil8",
        39: "depth16unorm",
        40: "depth24plus",
        41: "depth24plus-stencil8",
        42: "depth32float",
        43: "depth32float-stencil8",
        44: "bc1-rgba-unorm",
        45: "bc1-rgba-unorm-srgb",
        46: "bc2-rgba-unorm",
        47: "bc2-rgba-unorm-srgb",
        48: "bc3-rgba-unorm",
        49: "bc3-rgba-unorm-srgb",
        50: "bc4-r-unorm",
        51: "bc4-r-snorm",
        52: "bc5-rg-unorm",
        53: "bc5-rg-snorm",
        54: "bc6h-rgb-ufloat",
        55: "bc6h-rgb-float",
        56: "bc7-rgba-unorm",
        57: "bc7-rgba-unorm-srgb",
        58: "etc2-rgb8unorm",
        59: "etc2-rgb8unorm-srgb",
        60: "etc2-rgb8a1unorm",
        61: "etc2-rgb8a1unorm-srgb",
        62: "etc2-rgba8unorm",
        63: "etc2-rgba8unorm-srgb",
        64: "eac-r11unorm",
        65: "eac-r11snorm",
        66: "eac-rg11unorm",
        67: "eac-rg11snorm",
        68: "astc-4x4-unorm",
        69: "astc-4x4-unorm-srgb",
        70: "astc-5x4-unorm",
        71: "astc-5x4-unorm-srgb",
        72: "astc-5x5-unorm",
        73: "astc-5x5-unorm-srgb",
        74: "astc-6x5-unorm",
        75: "astc-6x5-unorm-srgb",
        76: "astc-6x6-unorm",
        77: "astc-6x6-unorm-srgb",
        78: "astc-8x5-unorm",
        79: "astc-8x5-unorm-srgb",
        80: "astc-8x6-unorm",
        81: "astc-8x6-unorm-srgb",
        82: "astc-8x8-unorm",
        83: "astc-8x8-unorm-srgb",
        84: "astc-10x5-unorm",
        85: "astc-10x5-unorm-srgb",
        86: "astc-10x6-unorm",
        87: "astc-10x6-unorm-srgb",
        88: "astc-10x8-unorm",
        89: "astc-10x8-unorm-srgb",
        90: "astc-10x10-unorm",
        91: "astc-10x10-unorm-srgb",
        92: "astc-12x10-unorm",
        93: "astc-12x10-unorm-srgb",
        94: "astc-12x12-unorm",
        95: "astc-12x12-unorm-srgb",
    },
    "TextureDimension": {
        0: "Undefined",
        1: "1d",
        2: "2d",
        3: "3d",
    },
    "PresentMode": {
        0: "Undefined",
        1: "Fifo",
        2: "FifoRelaxed",
        3: "Immediate",
        4: "Mailbox",
    },
    "CompositeAlphaMode": {
        0: "Auto",
        1: "Opaque",
        2: "Premultiplied",
        3: "Unpremultiplied",
        4: "Inherit",
    },
    "SurfaceGetCurrentTextureStatus": {
        1: "SuccessOptimal",
        2: "SuccessSuboptimal",
        3: "Timeout",
        4: "Outdated",
        5: "Lost",
        6: "OutOfMemory",
        7: "DeviceLost",
        8: "Error",
    },
}

native_flags = {
    "InstanceBackend.All": 0,
    "InstanceBackend.Vulkan": 1,
    "InstanceBackend.GL": 2,
    "InstanceBackend.Metal": 4,
    "InstanceBackend.DX12": 8,
    "InstanceBackend.DX11": 16,
    "InstanceBackend.BrowserWebGPU": 32,
    "InstanceBackend.Primary": 45,
    "InstanceBackend.Secondary": 18,
    "InstanceFlag.Default": 0,
    "InstanceFlag.Debug": 1,
    "InstanceFlag.Validation": 2,
    "InstanceFlag.DiscardHalLabels": 4,
}
