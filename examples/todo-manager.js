// Todo List Manager - Example of Copilot-generated code
// This demonstrates how Copilot can help build a complete feature

class TodoManager {
    constructor() {
        this.todos = [];
        this.nextId = 1;
    }

    // Add a new todo item
    addTodo(title, description = '') {
        const todo = {
            id: this.nextId++,
            title,
            description,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        return todo;
    }

    // Get all todos
    getAllTodos() {
        return [...this.todos];
    }

    // Get a specific todo by ID
    getTodoById(id) {
        return this.todos.find(todo => todo.id === id);
    }

    // Update a todo
    updateTodo(id, updates) {
        const todo = this.getTodoById(id);
        if (todo) {
            Object.assign(todo, updates);
            return todo;
        }
        return null;
    }

    // Delete a todo
    deleteTodo(id) {
        const index = this.todos.findIndex(todo => todo.id === id);
        if (index !== -1) {
            return this.todos.splice(index, 1)[0];
        }
        return null;
    }

    // Mark a todo as completed
    completeTodo(id) {
        const todo = this.getTodoById(id);
        if (todo) {
            todo.completed = true;
            todo.completedAt = new Date();
            return todo;
        }
        return null;
    }

    // Get only completed todos
    getCompletedTodos() {
        return this.todos.filter(todo => todo.completed);
    }

    // Get only pending todos
    getPendingTodos() {
        return this.todos.filter(todo => !todo.completed);
    }

    // Search todos by title
    searchTodos(searchTerm) {
        const term = searchTerm.toLowerCase();
        return this.todos.filter(todo => 
            todo.title.toLowerCase().includes(term) ||
            todo.description.toLowerCase().includes(term)
        );
    }

    // Clear all completed todos
    clearCompleted() {
        const completed = this.getCompletedTodos();
        this.todos = this.getPendingTodos();
        return completed;
    }
}

// Example usage
const manager = new TodoManager();

manager.addTodo('Learn GitHub Copilot', 'Complete all exercises');
manager.addTodo('Build a project', 'Create something awesome');
manager.addTodo('Share with friends', 'Show them what Copilot can do');

console.log('All todos:', manager.getAllTodos());

manager.completeTodo(1);
console.log('Completed todos:', manager.getCompletedTodos());
console.log('Pending todos:', manager.getPendingTodos());

// Try this yourself:
// 1. Add more methods (e.g., sorting, filtering by date)
// 2. Add priority levels to todos
// 3. Implement categories or tags
