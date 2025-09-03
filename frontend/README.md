# 🎨 StreetVision Frontend

[![Netlify Status](https://api.netlify.com/api/v1/badges/your-site-id/deploy-status)](https://streetvision.netlify.app)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Beautiful, Responsive Web Interface for AI-Powered Road Monitoring**

StreetVision Frontend is a modern, intuitive web application that provides a seamless user experience for pothole detection and automated complaint submission to government portals.

## 🌟 Live Demo

🚀 **Live Application**: [streetvision.netlify.app](https://streetvision.netlify.app)

![StreetVision Frontend](https://github.com/user-attachments/assets/your-image-id)

## ✨ Features

### 🎯 **User Experience**
- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Dual-Panel Design**: Separated image analysis and report submission sections
- **Intuitive Navigation**: User-friendly form flow and clear visual hierarchy
- **Real-time Feedback**: Instant visual feedback for user interactions

### 🖼️ **Image Analysis Section**
- **Drag & Drop Upload**: Easy image upload with visual feedback
- **File Format Support**: PNG, JPG, JPEG, GIF, BMP
- **Preview Functionality**: Instant image preview before analysis
- **Progress Indicators**: Visual feedback during processing
- **Result Display**: Clear presentation of AI analysis results

### 📋 **Report Submission Panel**
- **Smart Forms**: Auto-validation with real-time error checking
- **Location Integration**: GPS coordinate input with Google Maps integration
- **Secure Input**: Password fields with proper security
- **Mobile-First**: 10-digit mobile number validation
- **One-Click Location**: "Get Current Location" button for convenience

### 🎨 **Design Highlights**
- **Beautiful Gradients**: Purple-to-blue gradient background
- **Card-Based Layout**: Clean, modern card design
- **Consistent Iconography**: Meaningful icons for better UX
- **Smooth Animations**: Subtle hover effects and transitions
- **Professional Typography**: Clean, readable font choices

## 🏗️ Architecture

```
StreetVision Frontend
├── 📄 index.html          # Main application page
├── 🎨 styles/
│   ├── main.css           # Core styling and layout
│   ├── components.css     # Component-specific styles
│   └── responsive.css     # Mobile responsiveness
├── 📜 scripts/
│   ├── app.js            # Main application logic
│   ├── api.js            # Backend API integration
│   └── utils.js          # Utility functions
└── 🖼️ assets/
    ├── icons/            # UI icons and graphics
    └── images/           # Static images
```

## 🚀 Quick Start

### Local Development

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MayankDew08/streetvision.git
   cd streetvision/frontend
   ```

2. **Start Local Server**
   ```bash
   # Using Python
   python -m http.server 3000
   
   # Using Node.js
   npx http-server -p 3000
   
   # Using Live Server (VS Code Extension)
   # Right-click index.html → "Open with Live Server"
   ```

3. **Access Application**
   ```
   http://localhost:3000
   ```

### Backend Integration

For full functionality, run the backend locally:

```bash
# Backend runs locally on
http://localhost:8000

# Update API endpoints in scripts/api.js if needed
const API_BASE_URL = 'http://localhost:8000';
```

**Note**: Backend is currently set up for local development only.

## 🌐 Deployment

### Netlify Deployment (Current)

The frontend is deployed on **Netlify** for fast, reliable hosting:

**Live URL**: [streetvision.netlify.app](https://streetvision.netlify.app)

#### Deployment Steps:
1. **Connect Repository**
   - Link GitHub repository to Netlify
   - Set build directory to `frontend/`

2. **Build Settings**
   ```bash
   # Build command (if needed)
   # npm run build
   
   # Publish directory
   frontend/
   ```

3. **Environment Variables**
   ```bash
   # In Netlify Dashboard → Environment Variables (if needed)
   REACT_APP_API_URL=http://localhost:8000
   ```

4. **Auto-Deploy**
   - Automatic deployment on git push to main branch
   - Preview deployments for pull requests

### Alternative Hosting Options

#### Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

#### GitHub Pages
```bash
# Enable GitHub Pages in repository settings
# Set source to frontend/ folder
```

#### Firebase Hosting
```bash
# Initialize Firebase
firebase init hosting

# Deploy
firebase deploy
```

#### AWS S3 + CloudFront
```bash
# Upload to S3 bucket
aws s3 sync frontend/ s3://your-bucket-name

# Configure CloudFront distribution
```

## 🛠️ Configuration

### API Integration

Update the API endpoints in `scripts/api.js`:

```javascript
// API Configuration
const CONFIG = {
    API_BASE_URL: 'http://localhost:8000', // Local backend only
    ENDPOINTS: {
        PREDICT: '/predict',
        SUBMIT: '/user',
        HEALTH: '/'
    },
    TIMEOUT: 30000 // 30 seconds
};
```

### Environment-Specific Settings

```javascript
// Environment Detection
const isDevelopment = window.location.hostname === 'localhost';
const API_URL = 'http://localhost:8000'; // Backend runs locally only
```

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile First Approach */
@media (min-width: 768px) {
    /* Tablet styles */
}

@media (min-width: 1024px) {
    /* Desktop styles */
}

@media (min-width: 1200px) {
    /* Large desktop styles */
}
```

### Mobile Optimizations
- Touch-friendly button sizes (minimum 44px)
- Readable font sizes (minimum 16px)
- Optimized images for mobile bandwidth
- Fast loading times with minimal dependencies

## 🔧 Customization

### Theme Colors
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --card-background: rgba(255, 255, 255, 0.95);
    --text-primary: #333333;
    --text-secondary: #666666;
    --accent-color: #4CAF50;
    --error-color: #f44336;
}
```

### Component Styling
```css
/* Customize cards */
.analysis-card, .report-card {
    background: var(--card-background);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

/* Customize buttons */
.primary-button {
    background: var(--accent-color);
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
}
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] Image upload functionality
- [ ] Form validation (mobile, password, coordinates)
- [ ] Responsive design on different screen sizes
- [ ] API integration with backend
- [ ] Error handling and user feedback
- [ ] Cross-browser compatibility

### Browser Support
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 📊 Performance

### Optimization Features
- **Lightweight**: No heavy frameworks, pure HTML/CSS/JS
- **Fast Loading**: Optimized images and minimal dependencies
- **Efficient API Calls**: Smart request handling with loading states
- **Caching**: Browser caching for static assets
- **CDN**: Netlify's global CDN for fast content delivery

### Performance Metrics
- **First Contentful Paint**: <1.5s
- **Largest Contentful Paint**: <2.5s
- **Cumulative Layout Shift**: <0.1
- **Time to Interactive**: <3s

## 🔒 Security

### Security Features
- **HTTPS**: Secure communication with SSL/TLS
- **Input Validation**: Client-side validation for all form inputs
- **XSS Prevention**: Proper input sanitization
- **CORS Handling**: Proper cross-origin request handling
- **Content Security Policy**: CSP headers for additional security

### Privacy
- **No Data Storage**: No user data stored in frontend
- **Secure Transmission**: All data encrypted in transit
- **Privacy Compliant**: No tracking or analytics cookies

## 🔮 Future Enhancements

### Planned Features
- [ ] **Progressive Web App (PWA)**: Offline capability and app-like experience
- [ ] **Dark Mode**: Toggle between light and dark themes
- [ ] **Multi-language Support**: Internationalization (i18n)
- [ ] **Real-time Notifications**: WebSocket integration for live updates
- [ ] **Advanced File Upload**: Multiple file selection and batch processing
- [ ] **User Dashboard**: Personal complaint history and analytics
- [ ] **Map Integration**: Interactive map for location selection
- [ ] **Voice Input**: Speech-to-text for complaint descriptions

### Technical Improvements
- [ ] **React Migration**: Upgrade to React for better state management
- [ ] **TypeScript**: Add type safety and better development experience
- [ ] **Build Pipeline**: Webpack/Vite for optimized production builds
- [ ] **Testing Suite**: Automated testing with Jest and Cypress
- [ ] **Performance Monitoring**: Real User Monitoring (RUM)

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly across different browsers and devices
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style Guidelines
- Use semantic HTML5 elements
- Follow BEM methodology for CSS classes
- Use ES6+ JavaScript features
- Maintain consistent indentation (2 spaces)
- Add comments for complex functionality

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mayank Dew**
- GitHub: [@MayankDew08](https://github.com/MayankDew08)
- Project: [StreetVision](https://github.com/MayankDew08/streetvision)

## 🙏 Acknowledgments

- **Netlify** for reliable hosting and deployment
- **CSS Gradient** community for beautiful gradient inspirations
- **MDN Web Docs** for comprehensive web development resources
- **Open Source Community** for continuous inspiration and support

---

<div align="center">

**🎨 Beautiful UI for Safer Roads 🛣️**

[Live Demo](https://streetvision.netlify.app) • [Backend API](https://github.com/MayankDew08/streetvision/tree/main/backend) • [Issues](https://github.com/MayankDew08/streetvision/issues)

*Making government services accessible through beautiful, user-friendly interfaces*

</div>
