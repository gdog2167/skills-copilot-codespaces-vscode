# GitHub Copilot Quick Reference

A quick cheat sheet for using GitHub Copilot effectively.

## ⌨️ Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt + ]` | `Option + ]` |
| Previous suggestion | `Alt + [` | `Option + [` |
| Trigger inline suggestion | `Alt + \` | `Option + \` |
| Open Copilot panel | `Ctrl + Enter` | `Cmd + Enter` |

## 📝 Quick Commands

### Generate a Function
```javascript
// Function to [describe what it does]
function functionName(params) {
```

### Generate Tests
```javascript
// Test cases for [function name]
```

### Generate Documentation
```javascript
/**
 * [Type /** and press Enter above function]
 */
```

### Generate Sample Data
```javascript
// Array of 5 sample [data type] objects
const data = [
```

## 🎯 Comment Patterns That Work Well

### For Functions
```
// Function that [action] [input] and returns [output]
// Example: Function that takes an array of numbers and returns the average
```

### For Classes
```
// Class to represent a [concept] with [properties] and [methods]
// Example: Class to represent a User with name, email, and authentication methods
```

### For Complex Logic
```
// Algorithm to [goal]:
// 1. [step one]
// 2. [step two]
// 3. [step three]
```

## 🔍 Common Use Cases

### 1. String Manipulation
```javascript
// Convert string to title case
// Remove whitespace from string
// Check if string contains substring
```

### 2. Array Operations
```javascript
// Filter array by condition
// Map array elements
// Reduce array to single value
// Remove duplicates from array
```

### 3. API Calls
```javascript
// Fetch data from API endpoint
// Handle API errors gracefully
// Make authenticated API request
```

### 4. Data Validation
```javascript
// Validate email format
// Check if password meets requirements
// Validate phone number format
```

### 5. File Operations
```javascript
// Read file contents
// Write data to file
// Parse JSON from file
```

## 💡 Pro Tips

1. **Be Specific**: `// Sort array of users by age ascending` > `// Sort array`
2. **Use Examples**: Include example input/output in comments
3. **Name Well**: `calculateUserAge` > `calculate`
4. **One Task**: Break complex functions into smaller ones
5. **Review Always**: Never accept without reading

## 🚫 What NOT to Do

- ❌ Don't blindly accept all suggestions
- ❌ Don't use for security-critical code without review
- ❌ Don't rely on Copilot for algorithmic correctness
- ❌ Don't use vague comments
- ❌ Don't forget to test the generated code

## 📊 Language-Specific Hints

### JavaScript
```javascript
// Use async/await for promises
// Destructure objects in parameters
// Use arrow functions for callbacks
```

### Python
```python
# Use list comprehensions
# Follow PEP 8 naming conventions
# Add type hints for better suggestions
```

### TypeScript
```typescript
// Define interfaces for complex objects
// Use type annotations
// Leverage generics for reusable code
```

## 🎓 Learning Resources

- **In this repo**: Start with `GETTING_STARTED.md`
- **Practice**: Try exercises in `exercises/` folder
- **Examples**: Study code in `examples/` folder
- **Build**: Create projects in `projects/` folder

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| No suggestions | Wait 1-2 seconds, check Copilot status icon |
| Wrong suggestions | Be more specific in comments, add context |
| Copilot disabled | Click status icon, sign in to GitHub |
| Slow suggestions | Check internet connection |

## 📚 Where to Go Next

1. **Beginner**: Read `GETTING_STARTED.md`
2. **Learning**: Complete exercises in `exercises/`
3. **Improving**: Read `TIPS_AND_TRICKS.md`
4. **Building**: Start a project in `projects/`

---

**Remember**: Copilot is your coding assistant, not your replacement. You're still responsible for understanding, reviewing, and testing all code!

Happy coding! 🚀
