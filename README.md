
# 👚 Virtual Closet: AI Fashion Outfit Recommender

A sophisticated AI-powered fashion recommendation system that helps users build a virtual closet and get personalized outfit suggestions based on weather conditions and event types.

## 🚀 Features

### Core Functionality
- **Image Classification**: Automatically classifies uploaded clothing items using state-of-the-art vision models
- **Virtual Closet Management**: Stores clothing items with their visual embeddings for quick retrieval
- **Smart Outfit Generation**: Creates personalized outfit combinations based on weather and event context
- **AI-Powered Explanations**: Provides intelligent explanations for outfit choices using language models
- **Vector Database**: Efficient similarity search using FAISS for finding matching clothing items

### User Interface
- **Streamlit Web App**: Clean, intuitive interface for easy interaction
- **Image Upload**: Support for JPG, JPEG, and PNG formats
- **Real-time Classification**: Instant clothing type detection
- **Contextual Recommendations**: Weather and event-based outfit suggestions
- **Visual Feedback**: Clear display of uploaded images and results

## 🏗️ Architecture

### Components

#### 1. **Main Application (`main.py`)**
- Streamlit web interface
- Orchestrates all components
- Handles file uploads and user interactions
- Manages the complete workflow from upload to outfit generation

#### 2. **Image Classification (`classifier.py`)**
- Uses Hugging Face's DeiT (Data-efficient image Transformers) model
- Pre-trained on ImageNet for robust clothing classification
- Cached model loading for performance optimization
- Error handling for classification failures

#### 3. **Feature Extraction & Vector Database (`faiss_db.py`)**
- ResNet50-based feature extraction (2048-dimensional embeddings)
- FAISS vector database for efficient similarity search
- Persistent storage using pickle for closet data
- Metadata tracking for each clothing item

#### 4. **Outfit Generation (`outfit_suggester.py`)**
- Rule-based outfit generation system
- Context-aware recommendations (weather + event combinations)
- Scoring algorithm for item relevance
- Duplicate removal and fallback mechanisms

#### 5. **AI Explanations (`llm.py`)**
- Google Flan-T5 language model for natural language generation
- Fashion stylist persona for contextual explanations
- Structured prompts for consistent output
- Error handling for LLM failures

#### 6. **Image Processing (`utils.py`)**
- Standardized image preprocessing for ResNet50
- ImageNet normalization
- RGB conversion and resizing
- Tensor preparation for deep learning models

## 🛠️ Technology Stack

### Core Dependencies
- **PyTorch** (≥2.0.0): Deep learning framework
- **TorchVision** (≥0.15.0): Computer vision utilities
- **Transformers** (≥4.30.0): Hugging Face model library
- **FAISS** (≥1.7.4): Vector similarity search
- **Streamlit** (≥1.25.0): Web application framework
- **Pillow** (≥9.5.0): Image processing
- **Python-dotenv** (≥1.0.0): Environment variable management

### AI Models Used
- **DeiT (Data-efficient image Transformers)**: For clothing classification
- **ResNet50**: For feature extraction and embedding generation
- **Flan-T5**: For natural language outfit explanations

## 📁 Project Structure

```
fashion_recommender/
├── main.py                 # Main Streamlit application
├── classifier.py           # Image classification module
├── faiss_db.py            # Vector database management
├── outfit_suggester.py    # Outfit generation logic
├── llm.py                 # Language model for explanations
├── utils.py               # Image preprocessing utilities
├── requirements.txt       # Python dependencies
├── closet_db.pkl         # Persistent closet database
├── uploads/              # User uploaded images
│   ├── Screenshot 2025-07-07 at 7.54.03 PM.png
│   ├── Screenshot 2025-07-07 at 8.57.11 PM.png
│   ├── Screenshot 2025-07-07 at 8.56.52 PM.png
│   └── Screenshot 2025-07-07 at 8.57.04 PM.png
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Hugging Face API token (for model access)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fashion_recommender
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 🎯 How It Works

### 1. **Image Upload & Classification**
- User uploads a clothing image
- System automatically classifies the item using DeiT model
- Image is processed and stored with metadata

### 2. **Feature Extraction**
- ResNet50 extracts 2048-dimensional feature vectors
- Embeddings are stored in FAISS vector database
- Items are added to virtual closet with persistent storage

### 3. **Outfit Generation**
- User selects weather conditions and event type
- System generates contextual outfit recommendations
- Scoring algorithm prioritizes relevant items
- Duplicates are removed and results are limited to 3 items

### 4. **AI Explanation**
- Flan-T5 model generates natural language explanations
- Fashion stylist persona provides contextual reasoning
- Explains why each piece was chosen for the given context

## 🎨 Supported Features

### Weather Conditions
- ☀️ **Sunny**: Light, breathable clothing
- 🌧️ **Rainy**: Water-resistant and protective items
- ❄️ **Cold**: Warm, insulating layers

### Event Types
- 🏠 **Casual**: Comfortable, everyday wear
- 👔 **Formal**: Professional, sophisticated attire
- 🎉 **Party**: Stylish, statement pieces

### Clothing Classification
- Automatic detection of clothing types
- Support for various garment categories
- Real-time classification with confidence scores

## 🔧 Configuration

### Model Parameters
- **Feature Dimension**: 2048 (ResNet50 output)
- **Search Results**: 3 items per outfit
- **Max Tokens**: 100 for LLM explanations
- **Image Size**: 224x224 pixels (standard for ImageNet models)

### Database Settings
- **Storage Format**: Pickle (.pkl)
- **Index Type**: FAISS FlatL2
- **Persistence**: Automatic save/load

## 🐛 Troubleshooting

### Common Issues
1. **Hugging Face Token**: Ensure your API token is set in `.env`
2. **Model Loading**: Check internet connection for model downloads
3. **Memory Issues**: Large images may cause memory problems
4. **Classification Errors**: Ensure uploaded images are clear clothing items

### Error Handling
- Graceful degradation when models fail to load
- User-friendly error messages
- Fallback mechanisms for outfit generation
- Robust image processing with error recovery

## 📊 Performance

### Optimization Features
- **Model Caching**: Prevents repeated model loading
- **Vector Database**: Efficient similarity search
- **Image Preprocessing**: Optimized for deep learning models
- **Persistent Storage**: Maintains closet across sessions

### Scalability
- Modular architecture for easy component replacement
- Configurable parameters for different use cases
- Extensible outfit generation rules
- Support for multiple clothing categories

## 🔮 Future Enhancements

### Potential Improvements
- **Style Preferences**: User-specific style learning
- **Seasonal Recommendations**: Calendar-based suggestions
- **Social Features**: Sharing and rating outfits
- **Mobile App**: Native mobile application
- **AR Integration**: Virtual try-on capabilities
- **Brand Recognition**: Automatic brand detection
- **Sustainability**: Eco-friendly clothing recommendations

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

**Built with ❤️ using Streamlit, PyTorch, and Hugging Face Transformers**
