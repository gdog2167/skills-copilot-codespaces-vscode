# Getting Started with GitHub Copilot

Welcome! This guide will help you start your journey with GitHub Copilot.

## What is GitHub Copilot?

GitHub Copilot is your AI pair programmer. It uses machine learning to suggest code and entire functions in real-time, right from your editor.

## Prerequisites

- GitHub Copilot subscription (or free trial)
- VS Code or compatible editor
- GitHub Copilot extension installed

## Setup

1. **Install the GitHub Copilot Extension**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
   - Search for "GitHub Copilot"
   - Click Install
   - Sign in with your GitHub account

2. **Verify Installation**
   - Look for the Copilot icon in your status bar (bottom right)
   - It should show as active (no red X)

## Your First Steps

### Step 1: Try a Simple Example

1. Create a new file: `test.js`
2. Type this comment:
   ```javascript
   // function to add two numbers
   ```
3. Press Enter and wait
4. You should see gray text (Copilot's suggestion)
5. Press Tab to accept it!

### Step 2: Explore the Exercises

1. Open the `exercises/` folder
2. Start with `01-basic-functions.js`
3. Follow the instructions in each file
4. Practice accepting and rejecting suggestions

### Step 3: Learn Keyboard Shortcuts

- **Tab**: Accept suggestion
- **Esc**: Dismiss suggestion
- **Alt + ]** (or Option + ]): Next suggestion
- **Alt + [** (or Option + [): Previous suggestion
- **Alt + \** (or Option + \): Trigger inline suggestion

### Step 4: Build Something

1. Check out the `projects/` folder
2. Pick a starter project
3. Build it feature by feature with Copilot's help

## Tips for Success

### Write Good Comments

✅ Good:
```javascript
// Function that takes an array of numbers and returns the sum of only the even numbers
```

❌ Too vague:
```javascript
// sum function
```

### Use Descriptive Names

Copilot understands context from your variable and function names:

```javascript
// Copilot will understand this better
function calculateUserAverageScore(scores) {
    // Copilot can now suggest appropriate logic
}
```

### Break Down Complex Tasks

Instead of one large function, create smaller ones:

```javascript
// Step 1: Validate input
function validateEmail(email) {
    // Copilot suggests validation logic
}

// Step 2: Format input
function formatEmail(email) {
    // Copilot suggests formatting logic
}

// Step 3: Save to database
function saveEmail(email) {
    // Copilot suggests database logic
}
```

### Iterate on Suggestions

If the first suggestion isn't perfect:
1. Keep typing to refine
2. Try Alt + ] to see alternatives
3. Rephrase your comment
4. Add more context

## Common Patterns

### Pattern 1: Function from Comment
```javascript
// Function to check if a year is a leap year
function isLeapYear(year) {
    // Press Enter here and Copilot will suggest the logic
}
```

### Pattern 2: Test Generation
```javascript
function add(a, b) {
    return a + b;
}

// Write test cases for the add function
// Press Enter and Copilot will suggest tests
```

### Pattern 3: Documentation
```javascript
function complexCalculation(data, options) {
    // Implementation here
}

/**
 * Type /** above the function and press Enter
 * Copilot will generate JSDoc comments
 */
```

## Troubleshooting

### Copilot Not Working?

1. Check the Copilot icon in status bar
2. Click it and check for errors
3. Try signing out and back in
4. Restart VS Code

### Not Getting Suggestions?

1. Make sure you're in a supported file type (.js, .py, etc.)
2. Try being more specific in comments
3. Add more context (function names, variables)
4. Wait a moment - suggestions can take 1-2 seconds

### Suggestions Are Wrong?

That's normal! Copilot is a tool, not a replacement for your judgment:
1. Review all suggestions carefully
2. Test your code
3. Don't accept suggestions you don't understand
4. Modify suggestions to fit your needs

## Learning Path

1. **Week 1**: Complete exercises in `exercises/` folder
2. **Week 2**: Study examples in `examples/` folder
3. **Week 3**: Build a starter project in `projects/` folder
4. **Week 4**: Start your own project from scratch!

## Resources

- [Copilot Documentation](https://docs.github.com/en/copilot)
- [Best Practices Blog](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Copilot Tips](https://code.visualstudio.com/docs/editor/github-copilot)

## Next Steps

Ready to start? Here's your action plan:

1. ✅ Read this guide
2. 🎯 Open `exercises/01-basic-functions.js`
3. 💪 Complete all exercises
4. 🚀 Build your first project
5. 🎉 Share what you've learned!

Happy coding! Remember: Copilot is your assistant, not your replacement. You're still the developer, making the decisions and writing the code. Copilot just helps you do it faster!
