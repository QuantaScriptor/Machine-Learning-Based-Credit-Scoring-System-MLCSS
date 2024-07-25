# Machine Learning-Based Credit Scoring System (MLCSS)



## Description
Machine Learning-Based Credit Scoring System (MLCSS) is a machine learning algorithm designed to evaluate and score the creditworthiness of individuals.

## Offering
This project is available for purchase. For inquiries regarding pricing and licensing, please contact us at [reece.dixon@quantascript.com](mailto:reece.dixon@quantascript.com).

## Mathematical Equations

1. **Logistic Regression**: Predicting probability of default

   <p align="center">
   <math xmlns="http://www.w3.org/1998/Math/MathML">
     <mrow>
       <mi>P</mi>
       <mo>(</mo>
       <mi>y</mi>
       <mo>=</mo>
       <mn>1</mn>
       <mo>|</mo>
       <mi>X</mi>
       <mo>)</mo>
       <mo>=</mo>
       <mi>σ</mi>
       <mo>(</mo>
       <mi>X</mi>
       <mo>·</mo>
       <mi>β</mi>
       <mo>)</mo>
     </mrow>
   </math>
   </p>

2. **Random Forest**: Aggregating decision trees for classification

   <p align="center">
   <math xmlns="http://www.w3.org/1998/Math/MathML">
     <mrow>
       <mover>
         <mi>y</mi>
         <mo>^</mo>
       </mover>
       <mo>=</mo>
       <mfrac>
         <mn>1</mn>
         <mi>N</mi>
       </mfrac>
       <mrow>
         <munderover>
           <mo>∑</mo>
           <mi>i=1</mi>
           <mi>N</mi>
         </munderover>
         <mi>f</mi>
         <msub>
           <mi>i</mi>
         </msub>
         <mo>(</mo>
         <mi>X</mi>
         <mo>)</mo>
       </mrow>
     </mrow>
   </math>
   </p>

## Installation
To use MLCSS, you'll need to install the following dependencies:
- `numpy`
- `pandas`
- `scikit-learn`

You can install them using pip:
```bash
pip install numpy pandas scikit-learn
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/QuantaScriptor/Machine-Learning-Based-Credit-Scoring-System-MLCSS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Machine-Learning-Based-Credit-Scoring-System-MLCSS
   ```
3. Run the script:
   ```bash
   python mlcss.py
   ```

## License
This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.
