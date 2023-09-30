# Task-02: Terminal Wizard

## Part 1: Enter the maze

Clone Repository and Create "codes" Directory

1. Clone the GitHub repository:
    ```markdown
    git clone https://github.com/KshitijThareja/TerminalWizard.git
    ```

2. Create a new directory named "codes":
    ```markdown
    cd TerminalWizard
    mkdir codes
    ```

### First Challenge

3. Navigate to the directory:
    ```markdown
    cd directory_name
    ```


4. Save the secret code to Part_1.txt in the "codes" folder and commit changes:
    ```markdown
    touch Part_1.txt
    nano Part_1.txt and paste the code
    git add .
    git commit -m "Part 1 completed"
    git push origin master
    ```

## Part 2: Second Challenge

### Second Challenge

5. Navigate to the directory:
    ```markdown
    cd directory_name
    ```

6. Save the secret code to Part_2.txt in the "codes" folder and commit changes:
    ```markdown
    touch Part_2.txt
    nano Part_2.txt and paste the code
    git add .
    git commit -m "Part 2 completed"
    git push origin master
    ```

## Part 3: Third Challenge

### Switch  Branches

7. List all branches:
    ```markdown
    git branch -a
    ```

8. Switch to the branch named after Professor Lupin's subject:
    ```markdown
    git checkout <branch_name>
    ```

9. Copy the file from the other branch to the main branch and execute the python file:
    ```markdown
    git checkout <remote_branch> <relative_path_to_spell_file>
    python3 <spell_file>
    ```

10. Save the secret code to Part_3.txt in the "codes" folder and commit changes:
    ```markdown
    touch Part_3.txt
    nano Part_3.txt and paste the code
    git add .
    git commit -m "Part 3 completed"
    git push origin master
    ```
    
## Part 4: Fourth Challenge

### Fourth Challenge

11. View commit logs:
    ```markdown
    git log
    ```

12. Identify the commit with the spell:
    ```markdown
    git show <commit_hash>
    ```

13. Execute the spell file:
    ```markdown
    python <spell_file>
    ```

14. Save the secret code to Part_4.txt in the "codes" folder and commit changes:
    ```markdown
    touch Part_4.txt
    nano Part_4.txt and paste the code
    git add .
    git commit -m "Part 4 completed"
    git push origin master
    ```

## Part 5: The End

### Concatenate Files and Decode

15. Concatenate all part files into finalcode.txt:
    ```markdown
    cat task-01/codes/Part_* > task-01/codes/finalcode.txt
    ```

16. Remove individual part files:
    ```markdown
    rm task-01/codes/Part_*.txt
    ```

17. Decode the secret code using base64:
    ```markdown
    echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs" | base64 --decode > 
    ```

18. Commit and push final changes:
    ```markdown
    git add task-01/codes/finalcode.txt 
    git commit -m "Final code"
    git push origin master
    ```

## Final Task

### Clone Final Task Repository and Run Script

19. Clone the repository for the final task:
    ```markdown
    git clone 
    ```

20. Run the Python script in the terminal:
    ```markdown
    python3
    ```
## Screenshot:

![Victory](https://github.com/swayam-agrahari/amfoss-tasks/blob/master/task-01/codes/Screenshot.png)
