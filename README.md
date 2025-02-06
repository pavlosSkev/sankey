# sankey

### **How to Document the Input DataFrame Format?**  


- The DataFrame must contain the columns provided in `columns`.  
- Each column represents a stage in the flow, meaning the first column links to the second, the second links to the third, and so on.  
- The data should be categorical (strings or identifiers) rather than numerical.  
- Each row represents a **single flow path** in the Sankey diagram.  

---

### **Example**  

### **Expected DataFrame Format**
| table_input | project_name | job_name | table_output |
|-------------|-------------|----------|--------------|
| table_A     | project_1   | job_X    | table_B      |
| table_C     | project_2   | job_Y    | table_D      |
| table_A     | project_1   | job_X    | table_E      |

#### **Explanation**
- Each **row** represents a data flow.
- **Columns must be in the correct order**, representing the flow direction.
- Values should be **categorical** (e.g., table names, project names, job names).
- **Missing values are not supported** (or you can mention handling them if applicable).
