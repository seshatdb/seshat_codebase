from django.urls import path

from .models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real, Gdp_total, Gdp_growth_rate, Shares_of_world_gdp, Gdp_per_capita, Rate_of_gdp_per_capita_growth, Wages, Annual_wages, Rate_of_return, Famine_event, Disease_event, Jinshi_degrees_awarded, Examination, Taiping_rebellion, Worker_wage

from . import views

urlpatterns = [
    path('vars-old/', views.QingVarsOld, name='qing_vars_test'),
    path('vars/', views.QingVars, name='qing_vars'),
    path('playground/', views.playground, name='playground'),
]


urlpatterns += [
    path('population/create/', views.PopulationCreate.as_view(),
         name="population-create"),

    path('populations/', views.PopulationListView.as_view(), name='populations'),
    path('population/<int:pk>', views.PopulationDetailView.as_view(),
         name='population-detail'),
    path('population/<int:pk>/update/',
         views.PopulationUpdate.as_view(), name="population-update"),
    path('population/<int:pk>/delete/',
         views.PopulationDelete.as_view(), name="population-delete"),
    # Download
    path('populationdownload/', views.population_download,
         name="population-download"),
]

# GENERATIONS

# urlpatterns += [
#     path('population/create/', views.PopulationCreate.as_view(),
#          name="population-create"),

#     path('populations/', views.PopulationListView.as_view(), name='populations'),
#     path('population/<int:pk>', views.PopulationDetailView.as_view(),
#          name='population-detail'),
#     path('population/<int:pk>/update/',
#          views.PopulationUpdate.as_view(), name="population-update"),
#     path('population/<int:pk>/delete/',
#          views.PopulationDelete.as_view(), name="population-delete"),
#     # Download
#     path('populationdownload/', views.population_download,
#          name="population-download"),
# ]

urlpatterns += [
    path('land_taxes_collected/create/', views.Land_taxes_collectedCreate.as_view(),
         name="land_taxes_collected-create"),

    path('land_taxes_collecteds/', views.Land_taxes_collectedListView.as_view(),
         name='land_taxes_collecteds'),
    path('land_taxes_collected/<int:pk>', views.Land_taxes_collectedDetailView.as_view(),
         name='land_taxes_collected-detail'),
    path('land_taxes_collected/<int:pk>/update/',
         views.Land_taxes_collectedUpdate.as_view(), name="land_taxes_collected-update"),
    path('land_taxes_collected/<int:pk>/delete/',
         views.Land_taxes_collectedDelete.as_view(), name="land_taxes_collected-delete"),
    # Download
    path('land_taxes_collecteddownload/', views.land_taxes_collected_download,
         name="land_taxes_collected-download"),
]

urlpatterns += [
    path('land_yield/create/', views.Land_yieldCreate.as_view(),
         name="land_yield-create"),

    path('land_yields/', views.Land_yieldListView.as_view(), name='land_yields'),
    path('land_yield/<int:pk>', views.Land_yieldDetailView.as_view(),
         name='land_yield-detail'),
    path('land_yield/<int:pk>/update/',
         views.Land_yieldUpdate.as_view(), name="land_yield-update"),
    path('land_yield/<int:pk>/delete/',
         views.Land_yieldDelete.as_view(), name="land_yield-delete"),
    # Download
    path('land_yielddownload/', views.land_yield_download,
         name="land_yield-download"),
]

urlpatterns += [
    path('total_tax/create/', views.Total_taxCreate.as_view(),
         name="total_tax-create"),

    path('total_taxs/', views.Total_taxListView.as_view(), name='total_taxs'),
    path('total_tax/<int:pk>', views.Total_taxDetailView.as_view(),
         name='total_tax-detail'),
    path('total_tax/<int:pk>/update/',
         views.Total_taxUpdate.as_view(), name="total_tax-update"),
    path('total_tax/<int:pk>/delete/',
         views.Total_taxDelete.as_view(), name="total_tax-delete"),
    # Download
    path('total_taxdownload/', views.total_tax_download,
         name="total_tax-download"),
]

urlpatterns += [
    path('total_economic_output/create/', views.Total_economic_outputCreate.as_view(),
         name="total_economic_output-create"),

    path('total_economic_outputs/', views.Total_economic_outputListView.as_view(),
         name='total_economic_outputs'),
    path('total_economic_output/<int:pk>', views.Total_economic_outputDetailView.as_view(),
         name='total_economic_output-detail'),
    path('total_economic_output/<int:pk>/update/',
         views.Total_economic_outputUpdate.as_view(), name="total_economic_output-update"),
    path('total_economic_output/<int:pk>/delete/',
         views.Total_economic_outputDelete.as_view(), name="total_economic_output-delete"),
    # Download
    path('total_economic_outputdownload/', views.total_economic_output_download,
         name="total_economic_output-download"),
]

urlpatterns += [
    path('total_revenue/create/', views.Total_revenueCreate.as_view(),
         name="total_revenue-create"),

    path('total_revenues/', views.Total_revenueListView.as_view(),
         name='total_revenues'),
    path('total_revenue/<int:pk>', views.Total_revenueDetailView.as_view(),
         name='total_revenue-detail'),
    path('total_revenue/<int:pk>/update/',
         views.Total_revenueUpdate.as_view(), name="total_revenue-update"),
    path('total_revenue/<int:pk>/delete/',
         views.Total_revenueDelete.as_view(), name="total_revenue-delete"),
    # Download
    path('total_revenuedownload/', views.total_revenue_download,
         name="total_revenue-download"),
]

urlpatterns += [
    path('diding_taxes/create/', views.Diding_taxesCreate.as_view(),
         name="diding_taxes-create"),

    path('diding_taxess/', views.Diding_taxesListView.as_view(), name='diding_taxess'),
    path('diding_taxes/<int:pk>', views.Diding_taxesDetailView.as_view(),
         name='diding_taxes-detail'),
    path('diding_taxes/<int:pk>/update/',
         views.Diding_taxesUpdate.as_view(), name="diding_taxes-update"),
    path('diding_taxes/<int:pk>/delete/',
         views.Diding_taxesDelete.as_view(), name="diding_taxes-delete"),
    # Download
    path('diding_taxesdownload/', views.diding_taxes_download,
         name="diding_taxes-download"),
]

urlpatterns += [
    path('salt_tax/create/', views.Salt_taxCreate.as_view(),
         name="salt_tax-create"),

    path('salt_taxs/', views.Salt_taxListView.as_view(), name='salt_taxs'),
    path('salt_tax/<int:pk>', views.Salt_taxDetailView.as_view(),
         name='salt_tax-detail'),
    path('salt_tax/<int:pk>/update/',
         views.Salt_taxUpdate.as_view(), name="salt_tax-update"),
    path('salt_tax/<int:pk>/delete/',
         views.Salt_taxDelete.as_view(), name="salt_tax-delete"),
    # Download
    path('salt_taxdownload/', views.salt_tax_download,
         name="salt_tax-download"),
]

urlpatterns += [
    path('tariff_and_transit/create/', views.Tariff_and_transitCreate.as_view(),
         name="tariff_and_transit-create"),

    path('tariff_and_transits/', views.Tariff_and_transitListView.as_view(),
         name='tariff_and_transits'),
    path('tariff_and_transit/<int:pk>', views.Tariff_and_transitDetailView.as_view(),
         name='tariff_and_transit-detail'),
    path('tariff_and_transit/<int:pk>/update/',
         views.Tariff_and_transitUpdate.as_view(), name="tariff_and_transit-update"),
    path('tariff_and_transit/<int:pk>/delete/',
         views.Tariff_and_transitDelete.as_view(), name="tariff_and_transit-delete"),
    # Download
    path('tariff_and_transitdownload/', views.tariff_and_transit_download,
         name="tariff_and_transit-download"),
]

urlpatterns += [
    path('misc_incomes/create/', views.Misc_incomesCreate.as_view(),
         name="misc_incomes-create"),

    path('misc_incomess/', views.Misc_incomesListView.as_view(), name='misc_incomess'),
    path('misc_incomes/<int:pk>', views.Misc_incomesDetailView.as_view(),
         name='misc_incomes-detail'),
    path('misc_incomes/<int:pk>/update/',
         views.Misc_incomesUpdate.as_view(), name="misc_incomes-update"),
    path('misc_incomes/<int:pk>/delete/',
         views.Misc_incomesDelete.as_view(), name="misc_incomes-delete"),
    # Download
    path('misc_incomesdownload/', views.misc_incomes_download,
         name="misc_incomes-download"),
]

urlpatterns += [
    path('total_expenditure/create/', views.Total_expenditureCreate.as_view(),
         name="total_expenditure-create"),

    path('total_expenditures/', views.Total_expenditureListView.as_view(),
         name='total_expenditures'),
    path('total_expenditure/<int:pk>', views.Total_expenditureDetailView.as_view(),
         name='total_expenditure-detail'),
    path('total_expenditure/<int:pk>/update/',
         views.Total_expenditureUpdate.as_view(), name="total_expenditure-update"),
    path('total_expenditure/<int:pk>/delete/',
         views.Total_expenditureDelete.as_view(), name="total_expenditure-delete"),
    # Download
    path('total_expendituredownload/', views.total_expenditure_download,
         name="total_expenditure-download"),
]

urlpatterns += [
    path('balance/create/', views.BalanceCreate.as_view(),
         name="balance-create"),

    path('balances/', views.BalanceListView.as_view(), name='balances'),
    path('balance/<int:pk>', views.BalanceDetailView.as_view(),
         name='balance-detail'),
    path('balance/<int:pk>/update/',
         views.BalanceUpdate.as_view(), name="balance-update"),
    path('balance/<int:pk>/delete/',
         views.BalanceDelete.as_view(), name="balance-delete"),
    # Download
    path('balancedownload/', views.balance_download,
         name="balance-download"),
]

urlpatterns += [
    path('lijin/create/', views.LijinCreate.as_view(),
         name="lijin-create"),

    path('lijins/', views.LijinListView.as_view(), name='lijins'),
    path('lijin/<int:pk>', views.LijinDetailView.as_view(),
         name='lijin-detail'),
    path('lijin/<int:pk>/update/',
         views.LijinUpdate.as_view(), name="lijin-update"),
    path('lijin/<int:pk>/delete/',
         views.LijinDelete.as_view(), name="lijin-delete"),
    # Download
    path('lijindownload/', views.lijin_download,
         name="lijin-download"),
]

urlpatterns += [
    path('maritime_custom/create/', views.Maritime_customCreate.as_view(),
         name="maritime_custom-create"),

    path('maritime_customs/', views.Maritime_customListView.as_view(),
         name='maritime_customs'),
    path('maritime_custom/<int:pk>', views.Maritime_customDetailView.as_view(),
         name='maritime_custom-detail'),
    path('maritime_custom/<int:pk>/update/',
         views.Maritime_customUpdate.as_view(), name="maritime_custom-update"),
    path('maritime_custom/<int:pk>/delete/',
         views.Maritime_customDelete.as_view(), name="maritime_custom-delete"),
    # Download
    path('maritime_customdownload/', views.maritime_custom_download,
         name="maritime_custom-download"),
]

urlpatterns += [
    path('other_incomes/create/', views.Other_incomesCreate.as_view(),
         name="other_incomes-create"),

    path('other_incomess/', views.Other_incomesListView.as_view(),
         name='other_incomess'),
    path('other_incomes/<int:pk>', views.Other_incomesDetailView.as_view(),
         name='other_incomes-detail'),
    path('other_incomes/<int:pk>/update/',
         views.Other_incomesUpdate.as_view(), name="other_incomes-update"),
    path('other_incomes/<int:pk>/delete/',
         views.Other_incomesDelete.as_view(), name="other_incomes-delete"),
    # Download
    path('other_incomesdownload/', views.other_incomes_download,
         name="other_incomes-download"),
]

urlpatterns += [
    path('revenue_official/create/', views.Revenue_officialCreate.as_view(),
         name="revenue_official-create"),

    path('revenue_officials/', views.Revenue_officialListView.as_view(),
         name='revenue_officials'),
    path('revenue_official/<int:pk>', views.Revenue_officialDetailView.as_view(),
         name='revenue_official-detail'),
    path('revenue_official/<int:pk>/update/',
         views.Revenue_officialUpdate.as_view(), name="revenue_official-update"),
    path('revenue_official/<int:pk>/delete/',
         views.Revenue_officialDelete.as_view(), name="revenue_official-delete"),
    # Download
    path('revenue_officialdownload/', views.revenue_official_download,
         name="revenue_official-download"),
]

urlpatterns += [
    path('revenue_real/create/', views.Revenue_realCreate.as_view(),
         name="revenue_real-create"),

    path('revenue_reals/', views.Revenue_realListView.as_view(), name='revenue_reals'),
    path('revenue_real/<int:pk>', views.Revenue_realDetailView.as_view(),
         name='revenue_real-detail'),
    path('revenue_real/<int:pk>/update/',
         views.Revenue_realUpdate.as_view(), name="revenue_real-update"),
    path('revenue_real/<int:pk>/delete/',
         views.Revenue_realDelete.as_view(), name="revenue_real-delete"),
    # Download
    path('revenue_realdownload/', views.revenue_real_download,
         name="revenue_real-download"),
]

urlpatterns += [
    path('gdp_total/create/', views.Gdp_totalCreate.as_view(),
         name="gdp_total-create"),

    path('gdp_totals/', views.Gdp_totalListView.as_view(), name='gdp_totals'),
    path('GDP_total/<int:pk>', views.Gdp_totalDetailView.as_view(),
         name='GDP_total-detail'),
    path('GDP_total/<int:pk>/update/',
         views.Gdp_totalUpdate.as_view(), name="GDP_total-update"),
    path('GDP_total/<int:pk>/delete/',
         views.Gdp_totalDelete.as_view(), name="GDP_total-delete"),
    # Download
    path('GDP_totaldownload/', views.GDP_total_download,
         name="GDP_total-download"),
]

urlpatterns += [
    path('gdp_growth_rate/create/', views.Gdp_growth_rateCreate.as_view(),
         name="gdp_growth_rate-create"),

    path('gdp_growth_rates/', views.Gdp_growth_rateListView.as_view(),
         name='gdp_growth_rates'),
    path('GDP_growth_rate/<int:pk>', views.Gdp_growth_rateDetailView.as_view(),
         name='GDP_growth_rate-detail'),
    path('GDP_growth_rate/<int:pk>/update/',
         views.Gdp_growth_rateUpdate.as_view(), name="GDP_growth_rate-update"),
    path('GDP_growth_rate/<int:pk>/delete/',
         views.Gdp_growth_rateDelete.as_view(), name="GDP_growth_rate-delete"),
    # Download
    path('GDP_growth_ratedownload/', views.GDP_growth_rate_download,
         name="GDP_growth_rate-download"),
]

urlpatterns += [
    path('shares_of_world_gdp/create/', views.Shares_of_world_gdpCreate.as_view(),
         name="shares_of_world_gdp-create"),

    path('shares_of_world_gdps/', views.Shares_of_world_gdpListView.as_view(),
         name='shares_of_world_gdps'),
    path('shares_of_world_GDP/<int:pk>', views.Shares_of_world_gdpDetailView.as_view(),
         name='shares_of_world_GDP-detail'),
    path('shares_of_world_GDP/<int:pk>/update/',
         views.Shares_of_world_gdpUpdate.as_view(), name="shares_of_world_GDP-update"),
    path('shares_of_world_GDP/<int:pk>/delete/',
         views.Shares_of_world_gdpDelete.as_view(), name="shares_of_world_GDP-delete"),
    # Download
    path('shares_of_world_GDPdownload/', views.shares_of_world_GDP_download,
         name="shares_of_world_GDP-download"),
]

urlpatterns += [
    path('gdp/create/', views.Gdp_per_capitaCreate.as_view(),
         name="gdp_per_capita-create"),

    path('gdp_per_capitas/', views.Gdp_per_capitaListView.as_view(),
         name='gdp_per_capitas'),
    path('GDP_per_capita/<int:pk>', views.Gdp_per_capitaDetailView.as_view(),
         name='GDP_per_capita-detail'),
    path('GDP_per_capita/<int:pk>/update/',
         views.Gdp_per_capitaUpdate.as_view(), name="GDP_per_capita-update"),
    path('GDP_per_capita/<int:pk>/delete/',
         views.Gdp_per_capitaDelete.as_view(), name="GDP_per_capita-delete"),
    # Download
    path('GDP_per_capitadownload/', views.GDP_per_capita_download,
         name="GDP_per_capita-download"),
]

urlpatterns += [
    path('rate_of_gdp_per_capita_growth/create/', views.Rate_of_gdp_per_capita_growthCreate.as_view(),
         name="rate_of_gdp_per_capita_growth-create"),

    path('rate_of_gdp_per_capita_growths/', views.Rate_of_gdp_per_capita_growthListView.as_view(),
         name='rate_of_gdp_per_capita_growths'),
    path('rate_of_GDP_per_capita_growth/<int:pk>', views.Rate_of_gdp_per_capita_growthDetailView.as_view(),
         name='rate_of_GDP_per_capita_growth-detail'),
    path('rate_of_GDP_per_capita_growth/<int:pk>/update/',
         views.Rate_of_gdp_per_capita_growthUpdate.as_view(), name="rate_of_GDP_per_capita_growth-update"),
    path('rate_of_GDP_per_capita_growth/<int:pk>/delete/',
         views.Rate_of_gdp_per_capita_growthDelete.as_view(), name="rate_of_GDP_per_capita_growth-delete"),
    # Download
    path('rate_of_GDP_per_capita_growthdownload/', views.rate_of_GDP_per_capita_growth_download,
         name="rate_of_GDP_per_capita_growth-download"),
]

urlpatterns += [
    path('wages/create/', views.WagesCreate.as_view(),
         name="wages-create"),

    path('wagess/', views.WagesListView.as_view(), name='wagess'),
    path('wages/<int:pk>', views.WagesDetailView.as_view(),
         name='wages-detail'),
    path('wages/<int:pk>/update/',
         views.WagesUpdate.as_view(), name="wages-update"),
    path('wages/<int:pk>/delete/',
         views.WagesDelete.as_view(), name="wages-delete"),
    # Download
    path('wagesdownload/', views.wages_download,
         name="wages-download"),
]

urlpatterns += [
    path('annual_wages/create/', views.Annual_wagesCreate.as_view(),
         name="annual_wages-create"),

    path('annual_wagess/', views.Annual_wagesListView.as_view(), name='annual_wagess'),
    path('annual_wages/<int:pk>', views.Annual_wagesDetailView.as_view(),
         name='annual_wages-detail'),
    path('annual_wages/<int:pk>/update/',
         views.Annual_wagesUpdate.as_view(), name="annual_wages-update"),
    path('annual_wages/<int:pk>/delete/',
         views.Annual_wagesDelete.as_view(), name="annual_wages-delete"),
    # Download
    path('annual_wagesdownload/', views.annual_wages_download,
         name="annual_wages-download"),
]

urlpatterns += [
    path('rate_of_return/create/', views.Rate_of_returnCreate.as_view(),
         name="rate_of_return-create"),

    path('rate_of_returns/', views.Rate_of_returnListView.as_view(),
         name='rate_of_returns'),
    path('rate_of_return/<int:pk>', views.Rate_of_returnDetailView.as_view(),
         name='rate_of_return-detail'),
    path('rate_of_return/<int:pk>/update/',
         views.Rate_of_returnUpdate.as_view(), name="rate_of_return-update"),
    path('rate_of_return/<int:pk>/delete/',
         views.Rate_of_returnDelete.as_view(), name="rate_of_return-delete"),
    # Download
    path('rate_of_returndownload/', views.rate_of_return_download,
         name="rate_of_return-download"),
]

urlpatterns += [
    path('famine_event/create/', views.Famine_eventCreate.as_view(),
         name="famine_event-create"),

    path('famine_events/', views.Famine_eventListView.as_view(), name='famine_events'),
    path('famine_event/<int:pk>', views.Famine_eventDetailView.as_view(),
         name='famine_event-detail'),
    path('famine_event/<int:pk>/update/',
         views.Famine_eventUpdate.as_view(), name="famine_event-update"),
    path('famine_event/<int:pk>/delete/',
         views.Famine_eventDelete.as_view(), name="famine_event-delete"),
    # Download
    path('famine_eventdownload/', views.famine_event_download,
         name="famine_event-download"),
]

urlpatterns += [
    path('disease_event/create/', views.Disease_eventCreate.as_view(),
         name="disease_event-create"),

    path('disease_events/', views.Disease_eventListView.as_view(),
         name='disease_events'),
    path('disease_event/<int:pk>', views.Disease_eventDetailView.as_view(),
         name='disease_event-detail'),
    path('disease_event/<int:pk>/update/',
         views.Disease_eventUpdate.as_view(), name="disease_event-update"),
    path('disease_event/<int:pk>/delete/',
         views.Disease_eventDelete.as_view(), name="disease_event-delete"),
    # Download
    path('disease_eventdownload/', views.disease_event_download,
         name="disease_event-download"),
]

urlpatterns += [
    path('jinshi_degrees_awarded/create/', views.Jinshi_degrees_awardedCreate.as_view(),
         name="jinshi_degrees_awarded-create"),

    path('jinshi_degrees_awardeds/', views.Jinshi_degrees_awardedListView.as_view(),
         name='jinshi_degrees_awardeds'),
    path('jinshi_degrees_awarded/<int:pk>', views.Jinshi_degrees_awardedDetailView.as_view(),
         name='jinshi_degrees_awarded-detail'),
    path('jinshi_degrees_awarded/<int:pk>/update/',
         views.Jinshi_degrees_awardedUpdate.as_view(), name="jinshi_degrees_awarded-update"),
    path('jinshi_degrees_awarded/<int:pk>/delete/',
         views.Jinshi_degrees_awardedDelete.as_view(), name="jinshi_degrees_awarded-delete"),
    # Download
    path('jinshi_degrees_awardeddownload/', views.jinshi_degrees_awarded_download,
         name="jinshi_degrees_awarded-download"),
]

urlpatterns += [
    path('examination/create/', views.ExaminationCreate.as_view(),
         name="examination-create"),

    path('examinations/', views.ExaminationListView.as_view(), name='examinations'),
    path('examination/<int:pk>', views.ExaminationDetailView.as_view(),
         name='examination-detail'),
    path('examination/<int:pk>/update/',
         views.ExaminationUpdate.as_view(), name="examination-update"),
    path('examination/<int:pk>/delete/',
         views.ExaminationDelete.as_view(), name="examination-delete"),
    # Download
    path('examinationdownload/', views.examination_download,
         name="examination-download"),
]

urlpatterns += [
    path('taiping_rebellion/create/', views.Taiping_rebellionCreate.as_view(),
         name="taiping_rebellion-create"),

    path('taiping_rebellions/', views.Taiping_rebellionListView.as_view(),
         name='taiping_rebellions'),
    path('taiping_rebellion/<int:pk>', views.Taiping_rebellionDetailView.as_view(),
         name='taiping_rebellion-detail'),
    path('taiping_rebellion/<int:pk>/update/',
         views.Taiping_rebellionUpdate.as_view(), name="taiping_rebellion-update"),
    path('taiping_rebellion/<int:pk>/delete/',
         views.Taiping_rebellionDelete.as_view(), name="taiping_rebellion-delete"),
    # Download
    path('taiping_rebelliondownload/', views.taiping_rebellion_download,
         name="taiping_rebellion-download"),
]

urlpatterns += [
    path('worker_wage/create/', views.Worker_wageCreate.as_view(),
         name="worker_wage-create"),

    path('worker_wages/', views.Worker_wageListView.as_view(), name='worker_wages'),
    path('worker_wage/<int:pk>', views.Worker_wageDetailView.as_view(),
         name='worker_wage-detail'),
    path('worker_wage/<int:pk>/update/',
         views.Worker_wageUpdate.as_view(), name="worker_wage-update"),
    path('worker_wage/<int:pk>/delete/',
         views.Worker_wageDelete.as_view(), name="worker_wage-delete"),
    # Download
    path('worker_wagedownload/', views.worker_wage_download,
         name="worker_wage-download"),
]


# END OF GENERATIONS
urlpatterns += [
    path('playgrounddownload/', views.playgrounddownload,
         name="playgrounddownload"), ]
