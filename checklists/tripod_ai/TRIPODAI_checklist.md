# TRIPOD+AI Checklist

Version: 11-January-2024

| Section | Topic | Item | Development / evaluation | Checklist item | Reported on page |
|---------|-------|------|--------------------------|---------------|------------------|
| TITLE | Title | 1 | D;E | Identify the study as developing or evaluating the performance of a multivariable prediction model, the target population, and the outcome to be predicted |  |
| ABSTRACT | Abstract | 2 | D;E | See TRIPOD+AI for Abstracts checklist |  |
| INTRODUCTION | Background | 3a | D;E | Explain the healthcare context (including whether diagnostic or prognostic) and rationale for developing or evaluating the prediction model, including references to existing models |  |
| INTRODUCTION | Background | 3b | D;E | Describe the target population and the intended purpose of the prediction model in the context of the care pathway, including its intended users (e.g., healthcare professionals, patients, public) |  |
| INTRODUCTION | Background | 3c | D;E | Describe any known health inequalities between sociodemographic groups |  |
| INTRODUCTION | Objectives | 4 | D;E | Specify the study objectives, including whether the study describes the development or validation of a prediction model (or both) |  |
| METHODS | Data | 5a | D;E | Describe the sources of data separately for the development and evaluation datasets (e.g., randomised trial, cohort, routine care or registry data), the rationale for using these data, and representativeness of the data |  |
| METHODS | Data | 5b | D;E | Specify the dates of the collected participant data, including start and end of participant accrual; and, if applicable, end of follow-up |  |
| METHODS | Participants | 6a | D;E | Specify key elements of the study setting (e.g., primary care, secondary care, general population) including the number and location of centres |  |
| METHODS | Participants | 6b | D;E | Describe the eligibility criteria for study participants |  |
| METHODS | Participants | 6c | D;E | Give details of any treatments received, and how they were handled during model development or evaluation, if relevant |  |
| METHODS | Data preparation | 7 | D;E | Describe any data pre-processing and quality checking, including whether this was similar across relevant sociodemographic groups |  |
| METHODS | Outcome | 8a | D;E | Clearly define the outcome that is being predicted and the time horizon, including how and when assessed, the rationale for choosing this outcome, and whether the method of outcome assessment is consistent across sociodemographic groups |  |
| METHODS | Outcome | 8b | D;E | If outcome assessment requires subjective interpretation, describe the qualifications and demographic characteristics of the outcome assessors |  |
| METHODS | Outcome | 8c | D;E | Report any actions to blind assessment of the outcome to be predicted |  |
| METHODS | Predictors | 9a | D | Describe the choice of initial predictors (e.g., literature, previous models, all available predictors) and any pre-selection of predictors before model building |  |
| METHODS | Predictors | 9b | D;E | Clearly define all predictors, including how and when they were measured (and any actions to blind assessment of predictors for the outcome and other predictors) |  |
| METHODS | Predictors | 9c | D;E | If predictor measurement requires subjective interpretation, describe the qualifications and demographic characteristics of the predictor assessors |  |
| METHODS | Sample size | 10 | D;E | Explain how the study size was arrived at (separately for development and evaluation), and justify that the study size was sufficient to answer the research question. Include details of any sample size calculation |  |
| METHODS | Missing data | 11 | D;E | Describe how missing data were handled. Provide reasons for omitting any data |  |
| METHODS | Analytical methods | 12a | D | Describe how the data were used (e.g., for development and evaluation of model performance) in the analysis, including whether the data were partitioned, considering any sample size requirements |  |
| METHODS | Analytical methods | 12b | D | Depending on the type of model, describe how predictors were handled in the analyses (functional form, rescaling, transformation, or any standardisation). |  |
| METHODS | Analytical methods | 12c | D | Specify the type of model, rationale, all model-building steps, including any hyperparameter tuning, and method for internal validation |  |
| METHODS | Analytical methods | 12d | D;E | Describe if and how any heterogeneity in estimates of model parameter values and model performance was handled and quantified across clusters (e.g., hospitals, countries). See TRIPOD-Cluster for additional considerations |  |
| METHODS | Analytical methods | 12e | D;E | Specify all measures and plots used (and their rationale) to evaluate model performance (e.g., discrimination, calibration, clinical utility) and, if relevant, to compare multiple models |  |
| METHODS | Analytical methods | 12f | E | Describe any model updating (e.g., recalibration) arising from the model evaluation, either overall or for particular sociodemographic groups or settings |  |
| METHODS | Analytical methods | 12g | E | For model evaluation, describe how the model predictions were calculated (e.g., formula, code, object, application programming interface) |  |
| METHODS | Class imbalance | 13 | D;E | If class imbalance methods were used, state why and how this was done, and any subsequent methods to recalibrate the model or the model predictions |  |
| METHODS | Fairness | 14 | D;E | Describe any approaches that were used to address model fairness and their rationale |  |
| METHODS | Model output | 15 | D | Specify the output of the prediction model (e.g., probabilities, classification). Provide details and rationale for any classification and how the thresholds were identified |  |
| METHODS | Training versus evaluation | 16 | D;E | Identify any differences between the development and evaluation data in healthcare setting, eligibility criteria, outcome, and predictors |  |
| METHODS | Ethical approval | 17 | D;E | Name the institutional research board or ethics committee that approved the study and describe the participant-informed consent or the ethics committee waiver of informed consent |  |
| OPEN SCIENCE | Funding | 18a | D;E | Give the source of funding and the role of the funders for the present study |  |
| OPEN SCIENCE | Conflicts of interest | 18b | D;E | Declare any conflicts of interest and financial disclosures for all authors |  |
| OPEN SCIENCE | Protocol | 18c | D;E | Indicate where the study protocol can be accessed or state that a protocol was not prepared |  |
| OPEN SCIENCE | Registration | 18d | D;E | Provide registration information for the study, including register name and registration number, or state that the study was not registered |  |
| OPEN SCIENCE | Data sharing | 18e | D;E | Provide details of the availability of the study data |  |
| OPEN SCIENCE | Code sharing | 18f | D;E | Provide details of the availability of the analytical code |  |
| PATIENT & PUBLIC INVOLVEMENT | Patient & Public Involvement | 19 | D;E | Provide details of any patient and public involvement during the design, conduct, reporting, interpretation, or dissemination of the study or state no involvement. |  |
| RESULTS | Participants | 20a | D;E | Describe the flow of participants through the study, including the number of participants with and without the outcome and, if applicable, a summary of the follow-up time. A diagram may be helpful. |  |
| RESULTS | Participants | 20b | D;E | Report the characteristics overall and, where applicable, for each data source or setting, including the key dates, key predictors (including demographics), treatments received, sample size, number of outcome events, follow-up time, and amount of missing data. A table may be helpful. Report any differences across key demographic groups. |  |
| RESULTS | Participants | 20c | E | For model evaluation, show a comparison with the development data of the distribution of important predictors (demographics, predictors, and outcome). |  |
| RESULTS | Model development | 21 | D;E | Specify the number of participants and outcome events in each analysis (e.g., for model development, hyperparameter tuning, model evaluation) |  |
| RESULTS | Model specification | 22 | D | Provide details of the full prediction model (e.g., formula, code, object, application programming interface) to allow predictions in new individuals and to enable third-party evaluation and implementation, including any restrictions to access or re-use (e.g., freely available, proprietary) |  |
| RESULTS | Model performance | 23a | D;E | Report model performance estimates with confidence intervals, including for any key subgroups (e.g., sociodemographic). Consider plots to aid presentation. |  |
| RESULTS | Model performance | 23b | D;E | If examined, report results of any heterogeneity in model performance across clusters. See TRIPOD Cluster for additional details. |  |
| RESULTS | Model updating | 24 | E | Report the results from any model updating, including the updated model and subsequent performance |  |
| DISCUSSION | Interpretation | 25 | D;E | Give an overall interpretation of the main results, including issues of fairness in the context of the objectives and previous studies |  |
| DISCUSSION | Limitations | 26 | D;E | Discuss any limitations of the study (such as a non-representative sample, sample size, overfitting, missing data) and their effects on any biases, statistical uncertainty, and generalizability |  |
| DISCUSSION | Usability of the model in the context of current care | 27a | D | Describe how poor quality or unavailable input data (e.g., predictor values) should be assessed and handled when implementing the prediction model |  |
| DISCUSSION | Usability of the model in the context of current care | 27b | D | Specify whether users will be required to interact in the handling of the input data or use of the model, and what level of expertise is required of users |  |
| DISCUSSION | Usability of the model in the context of current care | 27c | D;E | Discuss any next steps for future research, with a specific view to applicability and generalizability of the model |  |

D=items relevant only to the development of a prediction model; E=items relating solely to the evaluation of a prediction model; D;E=items applicable to both the development and evaluation of a prediction model

From: Collins GS, Moons KGM, Dhiman P, et al. BMJ 2024;385:e078378. doi:10.1136/bmj-2023-078378
