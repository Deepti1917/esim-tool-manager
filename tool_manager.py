#!/usr/bin/env python3
"""
eSim Automated Tool Manager
Checks dependencies and provides CLI interface
"""

import subprocess
import sys
import platform
import os

class ToolManager:
    """Main class for managing eSim tools"""
    
    def __init__(self):
        self.os_type = platform.system()
        print(f"Detected OS: {self.os_type}")
        
        # List of tools eSim needs
        self.dependencies = {
            'Python': 'python3 --version',
            'Git': 'git --version',
            'Ngspice': 'ngspice --version',
            'Make': 'make --version'
        }
    
    def check_dependency(self, tool_name, command):
        """Check if a single tool is installed"""
        try:
            # Run the command to check version
            result = subprocess.run(
                command.split(), 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            
            if result.returncode == 0:
                # Tool is installed - get version
                version_info = result.stdout.split('\n')[0]
                return True, version_info
            else:
                return False, "Not found"
                
        except FileNotFoundError:
            return False, "Not installed"
        except subprocess.TimeoutExpired:
            return False, "Command timeout"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def check_all_dependencies(self):
        """Check all required dependencies"""
        print("\n" + "="*50)
        print("  eSim DEPENDENCY CHECKER")
        print("="*50 + "\n")
        
        results = {}
        missing_tools = []
        
        for tool_name, command in self.dependencies.items():
            print(f"Checking {tool_name}...", end=" ")
            is_installed, info = self.check_dependency(tool_name, command)
            
            results[tool_name] = {
                'installed': is_installed,
                'info': info
            }
            
            if is_installed:
                print(f"✓ FOUND")
                print(f"  Version: {info}")
            else:
                print(f"✗ MISSING")
                print(f"  Status: {info}")
                missing_tools.append(tool_name)
            print()
        
        # Summary
        print("="*50)
        total = len(self.dependencies)
        installed = total - len(missing_tools)
        print(f"Summary: {installed}/{total} tools found")
        
        if missing_tools:
            print(f"\nMissing tools: {', '.join(missing_tools)}")
            print("Please install missing tools before running eSim.")
        else:
            print("\n✓ All dependencies satisfied!")
        print("="*50 + "\n")
        
        return results
    
    def show_system_info(self):
        """Display system information"""
        print("\n" + "="*50)
        print("  SYSTEM INFORMATION")
        print("="*50)
        print(f"Operating System: {self.os_type}")
        print(f"OS Version: {platform.release()}")
        print(f"Machine: {platform.machine()}")
        print(f"Python Version: {sys.version.split()[0]}")
        print(f"Python Executable: {sys.executable}")
        print("="*50 + "\n")
    
    def show_menu(self):
        """Display main menu and handle user input"""
        while True:
            print("\n" + "="*50)
            print("  eSim AUTOMATED TOOL MANAGER")
            print("="*50)
            print("1. Check Dependencies")
            print("2. View System Information")
            print("3. View Installed Tools")
            print("4. Exit")
            print("="*50)
            
            try:
                choice = input("\nEnter your choice (1-4): ").strip()
                
                if choice == '1':
                    self.check_all_dependencies()
                    input("\nPress Enter to continue...")
                    
                elif choice == '2':
                    self.show_system_info()
                    input("\nPress Enter to continue...")
                    
                elif choice == '3':
                    self.list_tools()
                    input("\nPress Enter to continue...")
                    
                elif choice == '4':
                    print("\nThank you for using eSim Tool Manager!")
                    print("Exiting...\n")
                    break
                    
                else:
                    print("\n⚠ Invalid choice! Please enter 1, 2, 3, or 4.")
                    
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"\n⚠ Error: {e}")
    
    def list_tools(self):
        """List all tools being managed"""
        print("\n" + "="*50)
        print("  TOOLS MANAGED BY THIS TOOL")
        print("="*50)
        for i, tool in enumerate(self.dependencies.keys(), 1):
            print(f"{i}. {tool}")
        print("="*50 + "\n")


def main():
    """Main entry point"""
    print("\n🔧 Starting eSim Tool Manager...\n")
    
    try:
        manager = ToolManager()
        manager.show_menu()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()