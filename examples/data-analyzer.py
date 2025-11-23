# Data Analyzer - Example of Copilot-generated Python code
# Demonstrates statistical analysis and data processing

class DataAnalyzer:
    """A class to perform statistical analysis on numerical data"""
    
    def __init__(self, data=None):
        self.data = data if data else []
    
    def add_data(self, value):
        """Add a single value to the dataset"""
        self.data.append(value)
    
    def add_multiple(self, values):
        """Add multiple values to the dataset"""
        self.data.extend(values)
    
    def get_mean(self):
        """Calculate the mean (average) of the dataset"""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
    
    def get_median(self):
        """Calculate the median of the dataset"""
        if not self.data:
            return 0
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]
    
    def get_mode(self):
        """Find the most frequent value in the dataset"""
        if not self.data:
            return None
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        max_freq = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_freq]
        return modes[0] if len(modes) == 1 else modes
    
    def get_range(self):
        """Calculate the range (max - min) of the dataset"""
        if not self.data:
            return 0
        return max(self.data) - min(self.data)
    
    def get_variance(self):
        """Calculate the variance of the dataset"""
        if not self.data:
            return 0
        mean = self.get_mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    def get_std_deviation(self):
        """Calculate the standard deviation of the dataset"""
        return self.get_variance() ** 0.5
    
    def get_summary(self):
        """Get a complete statistical summary of the dataset"""
        return {
            'count': len(self.data),
            'mean': self.get_mean(),
            'median': self.get_median(),
            'mode': self.get_mode(),
            'range': self.get_range(),
            'variance': self.get_variance(),
            'std_deviation': self.get_std_deviation(),
            'min': min(self.data) if self.data else None,
            'max': max(self.data) if self.data else None
        }
    
    def filter_outliers(self, std_devs=2):
        """Remove outliers that are beyond specified standard deviations"""
        mean = self.get_mean()
        std = self.get_std_deviation()
        threshold = std_devs * std
        self.data = [x for x in self.data if abs(x - mean) <= threshold]
    
    def normalize(self):
        """Normalize data to 0-1 range"""
        if not self.data:
            return []
        min_val = min(self.data)
        max_val = max(self.data)
        if max_val == min_val:
            return [0] * len(self.data)
        return [(x - min_val) / (max_val - min_val) for x in self.data]


# Example usage
if __name__ == "__main__":
    # Sample dataset: test scores
    scores = [85, 92, 78, 95, 88, 76, 91, 84, 89, 93]
    
    analyzer = DataAnalyzer(scores)
    
    print("Statistical Analysis of Test Scores:")
    print("-" * 40)
    
    summary = analyzer.get_summary()
    for key, value in summary.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.2f}")
        else:
            print(f"{key.capitalize()}: {value}")
    
    print("\nNormalized scores:", [f"{x:.2f}" for x in analyzer.normalize()])
    
    # Try this yourself:
    # 1. Add methods for percentiles
    # 2. Implement data visualization
    # 3. Add support for grouped data analysis
    # 4. Create methods for correlation analysis
