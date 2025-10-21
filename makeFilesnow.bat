@echo off
REM ============================================
REM Project Setup Script for Windows
REM Global Commodity Shocks, Trade Linkages, and Economic Resilience
REM ============================================

echo ========================================
echo Creating Project Directory Structure
echo ========================================

REM Create main directories
mkdir data data\raw data\processed data\external
mkdir networks
mkdir src
mkdir notebooks
mkdir models
mkdir outputs outputs\figures outputs\tables outputs\data_quality
mkdir docs
mkdir presentations
mkdir reports reports\drafts
mkdir tests
mkdir logs

REM Create data subdirectories
mkdir data\raw\commodity_prices
mkdir data\raw\trade
mkdir data\raw\trade\comtrade_responses
mkdir data\raw\input_output
mkdir data\raw\macroeconomic
mkdir data\raw\global
mkdir data\raw\instruments

REM Create outputs subdirectories
mkdir outputs\figures\networks
mkdir outputs\figures\causal
mkdir outputs\figures\models
mkdir outputs\figures\scenarios
mkdir outputs\figures\exploratory
mkdir outputs\tables\network_metrics
mkdir outputs\tables\causal
mkdir outputs\tables\models
mkdir outputs\tables\scenarios

REM Create src subdirectories
mkdir src\data_collection
mkdir src\data_processing
mkdir src\network_analysis
mkdir src\causal_inference
mkdir src\feature_engineering
mkdir src\models
mkdir src\scenario_analysis
mkdir src\visualization
mkdir src\dashboard
mkdir src\dashboard\pages
mkdir src\dashboard\components

echo.
echo ========================================
echo Creating __init__.py files
echo ========================================

REM Create __init__.py for all Python packages
type nul > src\__init__.py
type nul > src\data_collection\__init__.py
type nul > src\data_processing\__init__.py
type nul > src\network_analysis\__init__.py
type nul > src\causal_inference\__init__.py
type nul > src\feature_engineering\__init__.py
type nul > src\models\__init__.py
type nul > src\scenario_analysis\__init__.py
type nul > src\visualization\__init__.py
type nul > src\dashboard\__init__.py
type nul > src\dashboard\components\__init__.py
type nul > tests\__init__.py

echo.
echo ========================================
echo Creating README.md
echo ========================================

(
echo # Global Commodity Shocks, Trade Linkages, and Economic Resilience
echo.
echo ## Project Overview
echo This project investigates how global commodity shocks ^(energy, food, metals^) transmit through India's international trade networks to affect domestic economic stability.
echo.
echo ## Project Structure
echo - **data/**: Raw and processed datasets
echo - **networks/**: Network graph objects and metrics
echo - **src/**: Source code for all analysis
echo - **notebooks/**: Jupyter notebooks for exploration
echo - **models/**: Saved trained models
echo - **outputs/**: All figures, tables, and reports
echo - **docs/**: Documentation and data dictionaries
echo - **presentations/**: Presentation slides
echo - **reports/**: Written reports
echo.
echo ## Setup Instructions
echo 1. Install Python 3.8+
echo 2. Run: `pip install -r requirements.txt`
echo 3. Download data using scripts in `src/data_collection/`
echo 4. Run analysis scripts in order
echo.
echo ## Team Members
echo - Lead: [Your Name]
echo - Member A: [Name]
echo - Member B: [Name]
echo - Member C: [Name]
echo.
echo ## License
echo [Add license information]
) > README.md

echo.
echo ========================================
echo Creating requirements.txt
echo ========================================

(
echo # Core Data Science
echo pandas==2.0.3
echo numpy==1.24.3
echo scipy==1.11.1
echo.
echo # Network Analysis
echo networkx==3.1
echo python-igraph==0.10.6
echo.
echo # Visualization
echo matplotlib==3.7.2
echo seaborn==0.12.2
echo plotly==5.15.0
echo.
echo # Statistical Analysis
echo statsmodels==0.14.0
echo linearmodels==5.1
echo.
echo # Machine Learning
echo scikit-learn==1.3.0
echo xgboost==1.7.6
echo.
echo # Deep Learning
echo tensorflow==2.13.0
echo torch==2.0.1
echo torch-geometric==2.3.1
echo.
echo # Data Collection
echo comtradeapicall==0.1.0
echo requests==2.31.0
echo beautifulsoup4==4.12.2
echo.
echo # Dashboard
echo streamlit==1.24.0
echo.
echo # Utilities
echo openpyxl==3.1.2
echo xlrd==2.0.1
echo python-dotenv==1.0.0
echo tqdm==4.65.0
echo.
echo # Jupyter
echo jupyter==1.0.0
echo ipykernel==6.25.0
) > requirements.txt

echo.
echo ========================================
echo Creating .gitignore
echo ========================================

(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo env/
echo venv/
echo ENV/
echo build/
echo develop-eggs/
echo dist/
echo downloads/
echo eggs/
echo .eggs/
echo lib/
echo lib64/
echo parts/
echo sdist/
echo var/
echo wheels/
echo *.egg-info/
echo .installed.cfg
echo *.egg
echo.
echo # Jupyter Notebook
echo .ipynb_checkpoints
echo.
echo # Data files (too large for Git)
echo data/raw/*.csv
echo data/raw/*.xlsx
echo data/raw/*.json
echo data/processed/*.csv
echo models/*.h5
echo models/*.pkl
echo models/*.pt
echo.
echo # Environment variables
echo .env
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo *~
echo.
echo # OS
echo .DS_Store
echo Thumbs.db
echo.
echo # Logs
echo logs/*.log
) > .gitignore

echo.
echo ========================================
echo Creating placeholder files
echo ========================================

REM Create placeholder data source documentation
(
echo # Data Sources
echo.
echo ## Commodity Prices
echo - **Source**: World Bank Pink Sheet
echo - **URL**: https://www.worldbank.org/en/research/commodity-markets
echo - **Coverage**: 2000-2025, Monthly
echo - **Variables**: Crude oil ^(Brent, Dubai^), Natural gas, Wheat, Rice, Copper, Aluminum
echo.
echo ## Bilateral Trade Data
echo - **Source**: UN Comtrade
echo - **URL**: https://uncomtrade.org/
echo - **Coverage**: 2010-2024, Monthly
echo - **Partners**: USA, China, EU27, Saudi Arabia, UAE, Qatar
echo - **Commodities**: HS 27 ^(Energy^), 10-11 ^(Food^), 74 ^(Copper^), 76 ^(Aluminum^)
echo.
echo ## Input-Output Tables
echo - **Source**: MOSPI ^(Ministry of Statistics India^)
echo - **URL**: https://mospi.gov.in/
echo - **Version**: 2015-16, 2020-21
echo - **Sectors**: 139 detailed sectors
echo.
echo ## Macroeconomic Data
echo - **Source**: Reserve Bank of India
echo - **URL**: https://dbie.rbi.org.in/
echo - **Variables**: IIP, WPI, GDP, Exchange Rate
echo.
echo ## Global Indicators
echo - **Source**: OECD Data Explorer
echo - **URL**: https://data-explorer.oecd.org/
echo - **Variables**: GDP growth, commodity indices, trade volumes
echo.
echo ## Instruments
echo - **OPEC**: https://www.opec.org/ ^(production quotas^)
echo - **NOAA**: https://www.cpc.ncep.noaa.gov/ ^(El Niño indices^)
) > docs\data_sources.md

REM Create basic Python template files
echo # Data collection utilities > src\data_collection\download_worldbank.py
echo # Data cleaning utilities > src\data_processing\clean_commodity_prices.py
echo # Network construction > src\network_analysis\build_trade_network.py
echo # IV analysis > src\causal_inference\instrumental_variables.py
echo # Feature engineering > src\feature_engineering\extract_network_features.py
echo # Model training > src\models\lstm_model.py
echo # Scenario analysis > src\scenario_analysis\historical_scenarios.py
echo # Visualization > src\visualization\plot_networks.py

echo.
echo ========================================
echo Creating virtual environment
echo ========================================

python -m venv venv

echo.
echo ========================================
echo Project Setup Complete!
echo ========================================
echo.
echo Next Steps:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Install requirements: pip install -r requirements.txt
echo 3. Start downloading data in data/raw/
echo 4. Begin with notebooks/01_data_exploration.ipynb
echo.
echo Directory structure created successfully!
echo.

pause