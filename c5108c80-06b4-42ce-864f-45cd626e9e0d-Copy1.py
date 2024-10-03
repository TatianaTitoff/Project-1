#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Татьяна, привет!👋</b>
# 
# Меня зовут Алексей Гриб, и я буду ревьюером твоего проекта. 
# 
# Сразу хочу предложить в дальнейшем общаться на "ты" - надеюсь, так будет комфортнее:) Но если это неудобно, обязательно дай знать, и мы придумаем что-нибудь ещё!
#     
# Цель ревью - не искать ошибки в твоём проекте, а помочь тебе сделать твою работу ещё лучше, устранив недочёты и приблизив её к реальным задачам специалиста по работе с данными. Поэтому не расстраивайся, если что-то не получилось с первого раза - это нормально, и это поможет тебе вырасти!
#     
# Ты можешь найти мои комментарии, обозначенные <font color='green'>зеленым</font>, <font color='gold'>желтым</font> и <font color='red'>красным</font> цветами, например:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> похвала, рекомендации «со звёздочкой», полезные лайфхаки, которые сделают и без того красивое решение ещё более элегантным.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> некритичные ошибки или развивающие рекомендации на будущее. 
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Критичные ошибки, которые обязательно нужно исправить.
# </div>
# 
# Я не смогу принять проект, если в нём будет хотя бы одна критичная ошибка или несколько некритичных ошибок - тогда проект нужно будет немного доработать. Но это нестрашно - я обязательно дам тебе подсказку или укажу верное направление.
#     
# Пожалуйста, не удаляй мои комментарии, они будут особенно полезны для нашей работы в случае повторной проверки проекта. 
#     
# Ты также можешь задавать свои вопросы, реагировать на мои комментарии, делать пометки и пояснения - полная творческая свобода! Но маленькая просьба - пускай они будут отличаться от моих комментариев, это поможет избежать путаницы в нашем общении:)
# Например, вот так:
#     
# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# *твой текст*
# </div>
#     
# Давай посмотрим на твой проект!

# <h1>Содержание<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Подготовка-данных" data-toc-modified-id="Подготовка-данных-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Подготовка данных</a></span></li><li><span><a href="#Анализ-данных" data-toc-modified-id="Анализ-данных-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Анализ данных</a></span><ul class="toc-item"><li><span><a href="#Распределение-металлов-в-сырье" data-toc-modified-id="Распределение-металлов-в-сырье-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Распределение металлов в сырье</a></span></li><li><span><a href="#Распределение-металлов-на-этапе-флотации" data-toc-modified-id="Распределение-металлов-на-этапе-флотации-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Распределение металлов на этапе флотации</a></span></li><li><span><a href="#Распределение-металлов-после-первичной-очистки." data-toc-modified-id="Распределение-металлов-после-первичной-очистки.-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Распределение металлов после первичной очистки.</a></span></li><li><span><a href="#Распределение-металлов-после-финальной-очистки." data-toc-modified-id="Распределение-металлов-после-финальной-очистки.-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Распределение металлов после финальной очистки.</a></span></li><li><span><a href="#Распределения-размеров-гранул-сырья-на-обучающей-и-тестовой-выборках." data-toc-modified-id="Распределения-размеров-гранул-сырья-на-обучающей-и-тестовой-выборках.-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Распределения размеров гранул сырья на обучающей и тестовой выборках.</a></span></li><li><span><a href="#Исследование-суммарной-концентрации-всех-веществ-на-разных-стадиях:-в-сырье,-в-черновом-и-финальном-концентратах." data-toc-modified-id="Исследование-суммарной-концентрации-всех-веществ-на-разных-стадиях:-в-сырье,-в-черновом-и-финальном-концентратах.-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Исследование суммарной концентрации всех веществ на разных стадиях: в сырье, в черновом и финальном концентратах.</a></span></li></ul></li><li><span><a href="#Модель" data-toc-modified-id="Модель-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Модель</a></span></li><li><span><a href="#Проверка-лучшей-модели-на-тестовой-выборке." data-toc-modified-id="Проверка-лучшей-модели-на-тестовой-выборке.-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Проверка лучшей модели на тестовой выборке.</a></span></li><li><span><a href="#Сравнение-с-константной-моделью." data-toc-modified-id="Сравнение-с-константной-моделью.-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Сравнение с константной моделью.</a></span></li><li><span><a href="#Выводы." data-toc-modified-id="Выводы.-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Выводы.</a></span></li></ul></div>

# # Восстановление золота из руды

# Подготовьте прототип модели машинного обучения для «Цифры». Компания разрабатывает решения для эффективной работы промышленных предприятий.
# 
# Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. Используйте данные с параметрами добычи и очистки. 
# 
# Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.
# 
# Вам нужно:
# 
# 1. Подготовить данные;
# 2. Провести исследовательский анализ данных;
# 3. Построить и обучить модель.
# 
# Чтобы выполнить проект, обращайтесь к библиотекам *pandas*, *matplotlib* и *sklearn.* Вам поможет их документация.

# <h1>План работы над проектом:<span class="tocSkip"></span></h1>
# 
# 1. Подготовьте данные
# 
# 1.1. Откройте файлы и изучите их.
# 
# Путь к файлам:
# 
# /datasets/gold_industry_train.csv. Скачать датасет
# 
# /datasets/gold_industry_test.csv. Скачать датасет
# 
# /datasets/gold_industry_full.csv. Скачать датасет
# 
# 1.2. Проверьте, что эффективность обогащения рассчитана правильно. 
# Вычислите её на обучающей выборке для признака rougher.output.recovery. Найдите MAE между вашими расчётами и значением признака. Опишите выводы.
# 
# 1.3. Проанализируйте признаки, недоступные в тестовой выборке. Что это за параметры? К какому типу относятся?
# 
# 1.4. Проведите предобработку данных.
# 
# 2. Проанализируйте данные
# 
# 2.1. Посмотрите, как меняется концентрация металлов (Au, Ag, Pb) на различных этапах: в сырье, в черновом концентрате, в концентрате после первой очистки и в финальном концентрате. Какие особенности имеют распределения? Опишите выводы.
# 
# 2.2.  Сравните распределения размеров гранул исходного сырья на обучающей и тестовой выборках. Если распределения сильно отличаются друг от друга, оценка модели будет неправильной.
# 
# 2.3. Исследуйте суммарную концентрацию металлов на разных стадиях: в сырье, в черновом концентрате, в концентрате после первой очистки и в финальном концентрате.
# 
# 3. Постройте модель
# 
# 3.1. Напишите функцию для вычисления итоговой sMAPE.
# 
# 3.2. Обучите разные модели и оцените их качество кросс-валидацией. Выберите лучшую модель и проверьте её на тестовой выборке. Опишите выводы.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Хорошее вступление!
#     
# В нём есть всё, что необходимо, чтобы понять суть проекта с первых строк отчёта!

# ## Подготовка данных

# In[1]:


#импортируем библиотеки
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer
from sklearn.pipeline import  make_pipeline
from numpy import arange
from sklearn.linear_model import Lasso, LassoCV
from sklearn.pipeline import Pipeline
from sklearn. model_selection import RepeatedKFold
import warnings
warnings.filterwarnings("ignore")


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Библиотеки импортировали - отлично!

# Загружаем выборки из файлов. Изучим информацию о данных.

# In[2]:


try:
    train=pd.read_csv('/datasets/gold_industry_train.csv', parse_dates = ['date'])
    test=pd.read_csv('/datasets/gold_industry_test.csv', parse_dates = ['date'])
    full=pd.read_csv('/datasets/gold_industry_full.csv', parse_dates = ['date']) 
except:
    print('Unknown Error')


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍</b> 
#     
# Данные загрузили. Круто, что сразу делаешь дату индексом:)
#     
# При считывании данных из файла здорово перестраховывать себя от ошибок, связанных, например, с неверным указанием пути к файлу. А иногда бывает, что работаешь с файлом локально, выгружаешь его на сервер, ожидая, что он будет принимать данные, которые лежат на том же сервере, а код падает с ошибкой, потому что путь к файлу не поменялся с локального на серверный.
#     
# Для этого, например, можно использовать конструкцию `try-except`: сначала пробуешь локальный путь, при возникновении ошибки используется серверный путь (подробнее можешь почитать тут: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html).
#     
# Но еще лучше использовать библиотеку `os` - её использование позволит тебе проверять существование указанных директорий (что может быть актуально при одновременной работа на локальном и сетевом окружении) и загружать данные из существующей директории, избегая ошибок. Как пример:
#     
#     import os
# 
#     pth1 = '/folder_1/data.csv'
#     pth2 = '/folder_2/data.csv'
#     
#     if os.path.exists(pth1):
#         query_1 = pd.read_csv(pth1)
#     elif os.path.exists(pth2):
#         query_1 = pd.read_csv(pth2)
#     else:
#         print('Something is wrong')

# In[3]:


train.info()


# In[4]:


test.info()


# In[5]:


full.info()


# В полной и обучающей выборках по 87 столбцов, в тестовой 53. В данных есть пропуски. Некоторые параметры недоступны, потому что замеряются и/или рассчитываются значительно позже. Из-за этого в тестовой выборке отсутствуют некоторые признаки, которые могут быть в обучающей. 

# In[6]:


train.isna().sum().sort_values()/len(train)


# В обучающей выборкеой пропущено не более 6,3% информации в каждом из столбцов. Сочтем возможным удалить такие строки для определения эффективности обогащения. 

# In[7]:


#recovery = train.dropna().reset_index() 
#len(recovery)/len(train)
#recovery = train


# In[8]:


#recovery.shape


# Всего удалилось 15,4% данных из обучающей выборки.

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# Удаление пропусков, тем не менее, лишает нас части данных для обучения модели - в нашем случае мы потеряли довольно большой кусок данных.
#         
# Лучше использовать методы заполнения предыдущим или следующим значением (из условий проекта мы знаем, что соседние значения похожи) или использовать инструменты машинного обучения для заполнения пропусков из семейства `sklearn.impute`.

# Проверим, что эффективность обогащения рассчитана правильно. Вычислим её на обучающей выборке для признака rougher.output.recovery. Найдем MAE между вашими расчётами и значением признака. Опишем выводы.

# In[9]:


rougher_output_recovery=train['rougher.output.recovery']
rougher_output_tail_au=train['rougher.output.tail_au']
rougher_input_feed_au=train['rougher.input.feed_au']
rougher_output_concentrate_au=train['rougher.output.concentrate_au']


# Напишем функцию для определения эффективности обогащения.

# In[10]:


def calc_rougher_output_recovery(rougher_output_concentrate,rougher_input_feed,rougher_output_tail):
    calc_rougher_output_recovery=abs((rougher_output_concentrate_au*(rougher_input_feed_au-rougher_output_tail_au))/(rougher_input_feed_au*(rougher_output_concentrate_au-rougher_output_tail_au)))*100
    return calc_rougher_output_recovery


# In[11]:


calc_rougher_output_recovery = calc_rougher_output_recovery(rougher_output_concentrate_au, rougher_input_feed_au,rougher_output_tail_au)


# In[12]:


train['rougher.output.recovery'].describe()


#  Найдем MAE между нашими расчётами и значением признака.

# In[13]:


mean_absolute_error (calc_rougher_output_recovery, rougher_output_recovery)


# In[14]:


round(mean_absolute_error(calc_rougher_output_recovery, rougher_output_recovery), 5)


# Абсолютное среднее получило значение близкое к 0, это значит, что расчеты можно считать корректными.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Обрати внимание, что `MAE` составила не `9.9`, а `9.9e-15`, то есть это значение настолько близкое к нулю, что после запятой цифры, отличные от нуля, начинаются только с пятнадцатого знака - эта ошибка, как правило, обсусловлена ошибкой округления при ручных расчётах. Вывод стоит подправить.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Проанализируем признаки, недоступные в тестовой выборке. Что это за параметры? К какому типу относятся?

# In[15]:


missing_cols=list(set(full.columns)-set(test.columns))
missing_cols=pd.Series(missing_cols)
missing_cols.sort_values()


# Отсутствующие столбцы в тестовой выборке - это выходные признаки после каждого технологического этапа.Среди них и наши целевые признаки final.output.recovery и rougher.output.recovery. Они понадобятся для подсчета метрики sMAPE.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Проанализировали разницу в признаках между выборками. 

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Здесь стоит вспомнить разницу между онлайн и оффлайн метриками: исходя из понимания, что тестовая выборка имитирует работу модели в реальных условиях протекания технологического процесса, давай подумаем, почему в `train` есть признаки, которые недоступны в `test`?
#     
# Нужно сделать вывод о причине расхожедния количества признаков между `train` и `test`.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Тестовая выборка, вероятно, создана на основе данных, пока не участвовавших в реальных технологических процессах, а потому в ней отсутствуют признаки, выявляемые после определенного технологического этапа, а также признаки, требующие калькуляции над такими признаками.

# Предобработка данных.

# In[16]:


display("Процент пропусков в обучающей выборке")
(train.isna().sum().sort_values()*100/len(train)).tail(20)


# In[17]:


display("Процент пропусков в полной выборке")
(full.isna().sum().sort_values()*100/len(full)).tail(20)


# Наибольшее количество пропусков наблюдается в столбцах, обозначающих выходные признаки после каждого технологического этапа. По условиям задачи соседние по времени параметры часто похожи. Заполним пропуски значениями, стоящими на строку выше пропущенных.

# In[18]:


full=full.fillna(method='ffill')
train=train.fillna(method='ffill') 


# In[19]:


full.isna().sum().sort_values()


# In[20]:


train.isna().sum().sort_values()


# Пропуски в обучающих и тестовых выборках заполнены.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Обработали пропуски с помощью стратегии заполнения `forward fill`, а также пояснили причину выбора такой стратегии - отлично!
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Здесь заканчивается стрктурный блок работы - стоит сделать промежуточные выводы о проделанной работе в блоке.

# ## Анализ данных

# Посмотрим, как меняется концентрация металлов (Au, Ag, Pb) на различных этапах очистки. Для этого создадим датасеты с концентрациями металлов на этапах флотации, первичной и финальной очистках.

# In[21]:


train_size0=len(train)
concetrates_primary=[]
concetrates_primary=pd.DataFrame(concetrates_primary)
concetrates_primary['rougher.input.feed_ag'] = full['rougher.input.feed_ag']
concetrates_primary['rougher.input.feed_pb'] = full['rougher.input.feed_pb']
concetrates_primary['rougher.input.feed_sol'] = full['rougher.input.feed_sol']
concetrates_primary['rougher.input.feed_au'] = full['rougher.input.feed_au']


# In[22]:


plt.figure(figsize=(18,12))
a=sns.set(style="whitegrid")
a=sns.boxplot(data=concetrates_primary)
plt.title('Концентрация металлов в сырье', fontsize=15)
plt.xlabel('Металл', fontsize=12)
plt.ylabel('Концентрация',fontsize=12);


# In[23]:


train=train.loc[train['rougher.input.feed_ag']>=3]
train=train.loc[(train['rougher.input.feed_pb']>=1) & (train['rougher.input.feed_pb']<=7)]
train=train.loc[(train['rougher.input.feed_sol']>=26) & (train['rougher.input.feed_sol']<=48)]
train=train.loc[train['rougher.input.feed_au']>=2]

train_size1=len(train)
train_size1*100/train_size0


# In[24]:


train_size1=len(train)
concetrates_rougher=[]
concetrates_rougher=pd.DataFrame(concetrates_rougher)
concetrates_rougher['rougher.output.concentrate_ag'] = full['rougher.output.concentrate_ag']
concetrates_rougher['rougher.output.concentrate_pb'] = full['rougher.output.concentrate_pb']
concetrates_rougher['rougher.output.concentrate_sol'] = full['rougher.output.concentrate_sol']
concetrates_rougher['rougher.output.concentrate_au'] = full['rougher.output.concentrate_au']
train_size1


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Судя по названию переменных, тут должен быть этап `rougher`, а не `primary_cleaner`.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[25]:


plt.figure(figsize=(18,12))
a=sns.set(style="whitegrid")
a=sns.boxplot(data=concetrates_rougher)
plt.title('Концентрация металлов после флотации', fontsize=15)
plt.xlabel('Металл', fontsize=12)
plt.ylabel('Концентрация',fontsize=12);


# In[26]:


train=train.loc[(train['rougher.output.concentrate_ag']>=6) & (train['rougher.output.concentrate_ag']<=18)]
train=train.loc[(train['rougher.output.concentrate_pb']>=4) & (train['rougher.output.concentrate_pb']<=12)]
train=train.loc[(train['rougher.output.concentrate_sol']>=20) & (train['rougher.output.concentrate_sol']<=38)]
train=train.loc[(train['rougher.output.concentrate_au']>=15) & (train['rougher.output.concentrate_au']<=26)]

train_size2=len(train)
train_size2*100/train_size1


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Тут и далее нужно подписать оси Х и Y, а также названия.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[27]:


concetrates_primary=[]
concetrates_primary=pd.DataFrame(concetrates_primary)
concetrates_primary['primary_cleaner.output.concentrate_ag'] = full['primary_cleaner.output.concentrate_ag']
concetrates_primary['primary_cleaner.output.concentrate_pb'] = full['primary_cleaner.output.concentrate_pb']
concetrates_primary['primary_cleaner.output.concentrate_sol'] = full['primary_cleaner.output.concentrate_sol']
concetrates_primary['primary_cleaner.output.concentrate_au'] = full['primary_cleaner.output.concentrate_au']


# In[28]:


plt.figure(figsize=(18,12))
a=sns.set(style="whitegrid")
a=sns.boxplot(data=concetrates_primary)
plt.title('Концентрация металлов после первичной очитски', fontsize=15)
plt.xlabel('Металл', fontsize=12)
plt.ylabel('Концентрация',fontsize=12);


# In[29]:


train=train.loc[(train['primary_cleaner.output.concentrate_ag']>=4) & (train['primary_cleaner.output.concentrate_ag']<=15)]
train=train.loc[(train['primary_cleaner.output.concentrate_pb']>=5) & (train['primary_cleaner.output.concentrate_pb']<=17)]
train=train.loc[train['primary_cleaner.output.concentrate_sol']<=23]
train=train.loc[(train['primary_cleaner.output.concentrate_au']>=24) & (train['primary_cleaner.output.concentrate_au']<=42)]

train_size3=len(train)
train_size3*100/train_size1


# In[30]:


concetrates_final=[]
concetrates_final=pd.DataFrame(concetrates_final)
concetrates_final['final.output.concentrate_ag']=train['final.output.concentrate_ag']
concetrates_final['final.output.concentrate_pb']=train['final.output.concentrate_pb']
concetrates_final['final.output.concentrate_sol']=train['final.output.concentrate_sol']
concetrates_final['final.output.concentrate_au']=train['final.output.concentrate_au']


# In[31]:


plt.figure(figsize=(18,12))
b=sns.set(style="whitegrid")
b=sns.boxplot(data=concetrates_final)
plt.title('Концентрация металлов после финальной очистки', fontsize=15)
plt.xlabel('Металл', fontsize=12)
plt.ylabel('Концентрация',fontsize=12);


# In[32]:


train=train.loc[(train['final.output.concentrate_ag']>=2) & (train['final.output.concentrate_ag']<=9)]
train=train.loc[(train['final.output.concentrate_pb']>=7) & (train['final.output.concentrate_pb']<=14)]
train=train.loc[(train['final.output.concentrate_sol']>=3) & (train['final.output.concentrate_sol']<=16)]
train=train.loc[(train['final.output.concentrate_au']>=21) & (train['final.output.concentrate_au']<=51)]

train_size4=len(train)
train_size4*100/train_size1


# В результате фильтрации данных мы очистили обучающую выборку от выбросов среди признаков, означающих % концентрации металлов на различных этапах разработки. Для обучения модели оставили чуть менее 80% данных.

# "Ящики с усами" показали, что больше всего выбросов в концентрации золота (AU) на стадиях первичной и финальной очистки. А так же очевидно, что среднее значение концентрации золота на финальной очистке вырастает по сравнению с предыдущими этапами.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Исследована концентрация металлов на разных стадиях обработки, проанализирована динамика концентрации в зависимости от этапа техпроцесса - отлично, тут всё верно.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Сверься с брифом проекта и добавь в исследование потерянный этап техпроцесса.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Не учтено: анализируется три этапа техпроцесса, должно быть четыре.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# ### Распределение металлов в сырье

# In[33]:


plt.title('Концентрация металлов в сырье', fontsize = 14)

train['rougher.input.feed_ag'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_ag')
train['rougher.input.feed_pb'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_pb')
train['rougher.input.feed_sol'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_sol')
train['rougher.input.feed_au'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_au')

plt.xlabel('% Концентрация')
plt.ylabel('Частота')
plt.show()


print('concentrate_ag = ', round(full['rougher.input.feed_ag'].mean(),2))
print('concentrate_pb = ', round(full['rougher.input.feed_pb'].mean(),2))
print('concentrate_sol = ', round(full['rougher.input.feed_sol'].mean(),2))
print('concentrate_au = ', round(full['rougher.input.feed_au'].mean(),2))


# ### Распределение металлов на этапе флотации

# In[34]:


plt.title('Концентрация металлов после флотации', fontsize = 14)

train['rougher.output.concentrate_ag'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_ag')
train['rougher.output.concentrate_pb'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_pb')
train['rougher.output.concentrate_sol'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_sol')
train['rougher.output.concentrate_au'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_au')

plt.xlabel('% Концентрация')
plt.ylabel('Частота')
plt.show()


print('concentrate_ag = ', round(full['rougher.output.concentrate_ag'].mean(),2))
print('concentrate_pb = ', round(full['rougher.output.concentrate_pb'].mean(),2))
print('concentrate_sol = ', round(full['rougher.output.concentrate_sol'].mean(),2))
print('concentrate_au = ', round(full['rougher.output.concentrate_au'].mean(),2))


# ### Распределение металлов после первичной очистки.

# In[35]:


plt.title('Концентрация металлов после первичной очистки', fontsize = 14)

train['primary_cleaner.output.concentrate_ag'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_ag')
train['primary_cleaner.output.concentrate_pb'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_pb')
train['primary_cleaner.output.concentrate_sol'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_sol')
train['primary_cleaner.output.concentrate_au'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_au')

plt.xlabel('% Концентрация металла')
plt.ylabel('Частота')
plt.show()


print('concentrate_ag = ', round(full['primary_cleaner.output.concentrate_ag'].mean(),2))
print('concentrate_pb = ', round(full['primary_cleaner.output.concentrate_pb'].mean(),2))
print('concentrate_sol = ', round(full['primary_cleaner.output.concentrate_sol'].mean(),2))
print('concentrate_au = ', round(full['primary_cleaner.output.concentrate_au'].mean(),2))


# ### Распределение металлов после финальной очистки.

# In[36]:


plt.title('Концентрация металлов после финальной очистки', fontsize = 14)

train['final.output.concentrate_ag'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_ag')
train['final.output.concentrate_pb'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_pb')
train['final.output.concentrate_sol'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_sol')
train['final.output.concentrate_au'].plot(kind='hist',figsize=(12,6),grid=True, legend=True, histtype='step', linewidth=3, label='concentrate_au')

plt.xlabel('% Концентрация металла')
plt.ylabel('Частота')
plt.show()

print('concentrate_ag = ', round(full['final.output.concentrate_ag'].mean(),2))
print('concentrate_pb = ', round(full['final.output.concentrate_pb'].mean(),2))
print('concentrate_sol = ', round(full['final.output.concentrate_sol'].mean(),2))
print('concentrate_au = ', round(full['final.output.concentrate_au'].mean(),2))


# В результате первичной очистки в 3 раза сократилось содержание sol, в том время как содержание золота росло почти в 1,5 раза с каждым этапом обработки.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На данном этапе следует также избавиться от аномалий - предполагается, что на этапе анализа суммарной концентрации аномалии уже были обнаружены и удалены. Давай обратим внимание на левую сторону графика по оси Х - все ли значения, которые мы там видим, кажутся адекватными?
#     
# Обрати внимание, что ты анализируешь суммарную концентрацию на `full` выборке, а удалить аномалии важно из `train`, так как на этой выборке мы будем обучать модели, и нам важно обеспечить её чистоту.
#     
# Тут можно пойти двумя путями:
# - если из `train` уже были удалены лишние столбцы, то суммарную концентрацию напрямую не выйдет отфильтровать - в таком случае нужно удалить аномалии из `full`, а потом использовать столбец `date` для очистки `train`: в `train` нужно будет оставить только те строки, `date` которых есть в столбце `date` у `full` выборки - так как из `full` уже будут удалены аномалии, то и дата аномальных замеров будет удалена;
# - если из `train` ещё не были удалены лишние признаки, то можно очистить `train` напрямую.
#     
# Также потерян один этап техпроцесса.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# ### Распределения размеров гранул сырья на обучающей и тестовой выборках.

# In[37]:


plt.title('Feed size input', fontsize = 14)

sns.histplot(data=train['primary_cleaner.input.feed_size'], stat='density', alpha = 0.8)
sns.histplot(data=test['primary_cleaner.input.feed_size'], stat='density', alpha = 0.3, color = 'red')


plt.xlabel('Feed size')
plt.ylabel('Friqency')
plt.show()


# In[38]:


test['primary_cleaner.input.feed_size'].describe()


# In[39]:


train['primary_cleaner.input.feed_size'].describe()


# Отметим, что размеры гранул сырья в обучающей и тестовой выборках распределелись идентичным образом.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 1. Линейный график не подходит для сравнения распределений - нужно использовать гистограммы.
# 2. Здесь мы имеем дело с непрерывной величиной - для анализа её распределения стоит использовать нормированную гистограмму (например, `shs.histplot()` с параметром `stat='density'` или `sns.kdeplot()`): гистограммы такого типа позволяют нивелировать разницу в размерах выборок при анализе распределений. Обрати также внимание, что при использовании нормированных гистограмм по оси Y будет уже не частота значений, а плотность распределения.
# 3. Сверья с брифом проекта и убедись, что ты исследуешь нужный этап техпроцесса.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# ### Исследование суммарной концентрации всех веществ на разных стадиях: в сырье, в черновом и финальном концентратах.

# Суммарная концентрация металлов в сырье.

# In[40]:


train['sum_concentrate_primary']=train['rougher.input.feed_ag']+train['rougher.input.feed_pb']+train['rougher.input.feed_sol']+train['rougher.input.feed_au']


# Суммарная концентрация веществ после флотации.

# In[41]:


train['sum_concentrate_rougher']=train['rougher.output.concentrate_ag']+train['rougher.output.concentrate_pb']+train['rougher.output.concentrate_sol']+train['rougher.output.concentrate_au']


# Суммарная концентрация веществ после первичной очистки.

# In[42]:


train['sum_primary_cleaner_output_concentrate']=train['primary_cleaner.output.concentrate_ag']+train['primary_cleaner.output.concentrate_pb']+train['primary_cleaner.output.concentrate_sol']+train['primary_cleaner.output.concentrate_au']


# Суммарная концентрация веществ после финальной очистки.

# In[43]:


train['sum_final_output_concentrate']=train['final.output.concentrate_ag']+train['final.output.concentrate_pb']+train['final.output.concentrate_sol']+train['final.output.concentrate_au']


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Сверься с брифом проекта и добавь в исследование потерянный этап техпроцесса.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Не учтено: анализируется три этапа техпроцесса, должно быть четыре.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[44]:


plt.title('Концентрация металлов по этам процесса', fontsize = 14)

train['sum_concentrate_rougher'].plot(kind='hist',figsize=(12,8),grid=True, legend=True, histtype='step', linewidth=3, label='sum_concentrate_rougher')
train['sum_primary_cleaner_output_concentrate'].plot(kind='hist',figsize=(12,8),grid=True, legend=True, histtype='step', linewidth=3, label='sum_primary_cleaner_output_concentrate')
train['sum_final_output_concentrate'].plot(kind='hist',figsize=(12,8),grid=True, legend=True, histtype='step', linewidth=3, label='sum_final_output_concentrate')
train['sum_concentrate_primary'].plot(kind='hist',figsize=(12,8),grid=True, legend=True, histtype='step', linewidth=3, label='sum_input_primary_concentrate')

plt.xlabel('% Сумма концентраций металлов')
plt.ylabel('Частота')
plt.show()

print('sum_input_primary_concentrate = ', round(train['sum_concentrate_primary'].mean(),2))
print('sum_concentrate_rougher = ', round(train['sum_concentrate_rougher'].mean(),2))
print('sum_primary_cleaner_output_concentrate = ', round(train['sum_primary_cleaner_output_concentrate'].mean(),2))
print('sum_final_output_concentrate = ', round(train['sum_final_output_concentrate'].mean(),2))


# По гистраграмме и средним значениям концентрации металлов можем отметить, что после флотации содержание металлов возросло на 20% по сравнению с сырьем, после первичной очистки концетрация металлов снижается в среднем на 7-8 %, зато после финальной очистки вырастает на 7-8%, и как нам известно из анализа выше, в основном за счет увеличения концентрации золота.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Исследована суммарная концентрация металлов на разных стадиях техпроцесса - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Нужно сделать вывод о динамике суммарной концентрации металлов.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Комментарии о нулевых значениях и их удаление должны быть на этапе анализа индивидуальной концентрации каждого металла - предполагается, что эти аномалии должны были быть замечены ранее, прокомментированы и удалены, и уже на этапе суммарной концентрации мы имеем дело с очищенными данными.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Здесь заканчивается стрктурный блок работы - стоит сделать промежуточные выводы о проделанной работе в блоке.

# ## Модель

# Определим функцию для расчета метрики качества sMAPE и промежуточную функцию sMAPE_i.

# In[45]:


def sMAPE_i (target, predict):    
    sMAPE_i=np.mean(abs(target-predict)/((abs(target)+abs(predict))/2))*100
    
    return sMAPE_i


# In[46]:


def sMAPE(sMAPE_rougher, sMAPE_final):
    
    sMAP=0.25*sMAPE_rougher+0.75*sMAPE_final
    return sMAP


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть функция для оценки `sMAPE` - супер!
# </div>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Расчёт двух частей метрики дублируется - его стоит вынести в отдельную функцию и вызывать внутри твоей основной функции, чтобы решение было гибким и масштабируемым, а также чтобы не допускать дублирование кода.
#     

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Тренировать модель будем только на тех столбцах обучающей выборке, которые содержатся в датафрейме с тестовыми.
# Целевые признаки rougher.output.recovery и final.output.recovery.

# In[47]:


feature=train[test.columns]


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Синхронизировали тренировочную и тестовую выборки по набору признаков - хорошо!
# </div>

# In[48]:


feature=feature.drop('date',axis=1)
feature.columns


# In[49]:


target=train[['rougher.output.recovery','final.output.recovery']]
target_rougher=train['rougher.output.recovery']
target_final=train['final.output.recovery']


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выделили признаки для обучения и целевые признаки - отлично!
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# Дополнительно стоит выполнить масштабирование непрерывных переменных - это важно для линейной регрессии, которую ты используешь.

# Произведем кросс-валидацию для модели Линейной регрессии.

# In[50]:


model_rougher_LR=LinearRegression()
model_final_LR=LinearRegression()
scores_rougher = cross_val_score(model_rougher_LR, feature, target_rougher, cv=5, scoring=make_scorer(sMAPE_i, greater_is_better=False))
scores_final = cross_val_score(model_final_LR, feature, target_final, cv=5, scoring=make_scorer(sMAPE_i, greater_is_better=False))
scores_rougher_mean = abs(pd.Series(scores_rougher).mean())
scores_final_mean = abs(pd.Series(scores_final).mean())
display("Среднее sMAPE модели Линейной регрессии")
display("Флотация", scores_rougher_mean)
display("Финальная очистка", scores_final_mean)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b>
#     
# Оценили линейную регрессию на кросс-валидации - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b>
# На сборном проекте от студентов ожидается умение пользоваться автоматизированным средствами проведения кросс-валидации - для этого можно использовать:
# - `cross_val_score` (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html), `cross_validate` (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate) или `cross_val_predict` (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict) для проведения кросс-валидации без встроенной оптимизации гиперпараметров (при этом их можно использовать в цикле для оптимизации гиперпараметров);
# - `GridSearchCV` (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), `RandomizedSearchCV` (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV) или аналоги для проведения кросс-валидации и одновременной оптимизации гиперпараметров (предпочительнее).
#         
# Довольно важным моментом является настройка параметра `scoring` - именно он отвечает за метрику, которая будет оценивать качество моделей в ходе кросс-валидации (в том числе при оптимизации гиперпараметров). Если не настроить его, оценка моделей на кросс-валидации будет выполнена по дефолтной метрике регрессионных моделей - `R2`.
#     
# Метрика нашего проекта - `sMAPE`, и в базовом наборе метрик `sklearn` она отсутствует - нам придётся сделать свой скорринг. Для этого можно использовать инструмент `make_scorer` (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html).
#     
# Так как метрика `sMAPE` применяется для задач регрессии, то она тем лучше, чем ниже - это нужно учитывать при создании скорринга для кросс-валидации, так как по умолчанию инструменты кросс-валидации вроде `cross_val_score` и `GridSearchCV/RandomizedSearchCV` умеют только максимизировать метрику качества. Поэтому при создании скорринга с помощью `make_scorer` важно настроить параметр `greater_is_better=False`, чтобы оптимизируемая метрика минимизировалась, а не максимизировалась - таким образом задача максимизации будет решаться через задачу минимизации обратной функции.
#     
# Также при настройке этого параметра получаемая метрика будет отрицательной: это особеность работы `make_scorer` с настроенным параметром `greater_is_better=False`. Поэтому при выводе метрики на экран её стоит сделать положительной: взять по модулю, домножить на `-1` или просто указать `-` при выводе на экран, вроде `print(-a)`.
# </div>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 1. Из `scores_` нужно брать среднее, а не минимальное значение - нас интересует агегированная оценка по всем фолдам, а не только по лучшему.
# 2. Знак метрики некорректный.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Из двух оценок `sMAPE` на кросс-валидации нужно посчитать итоговую оценку для `sMAPE`.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На этой итерации модельный блок списан из https://github.com/sxemixa/Gold-recovery/blob/main/Gold%20recovery.ipynb. Нужно переделать с нуля и выполнить следующие допзадания:
# - дополнительно исследовать `Lasso`, `ElasticNet`: для линейных моделей оптимизировать один гиперпараметр, для случайного леса и дерева решений - не менее двух;
# - работу с пайплайном организовать через `Pipeline` (https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) вместо текущего `make_pipeline`, в составе пайплайна вместо `StandardScaler` выполнить шкалирование переменных через `MinMaxScaler`;
# - помимо `sMAPE`, дополнительно посчитать метрики `MAE` и `RMSE` на кросс-валидации (для этого настроить параметры `scoring` и `refit` у `GridSearchCV`), результаты вместо `best_score_` получить из `cv_resulst_` по лучшему индексу (всю требуемую информацию можно получить из документации `GridSearchCV`). 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Исследуем 4 типа моделей, оптимизируем для линейных 1 гиперпараметр, для случайного леса и дерева решений по 2. Настройку гиперпараметров будем подгонять под лучшие значения функций: mae, mape, rmse.В параметре refit укажем функцию mape для финальной подгонки моделей.

# In[51]:


from sklearn.linear_model import ElasticNet


# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b>
# Все библиотеки стоит импортировать в начале проекта - таким образом получатель твоего отчёта сможет узнать о проблемах с его окружением сразу перед работой с проектом, а не посреди или в конце проекта.

# In[52]:


alphas=list(np.arange(0.1,2,0.05))
depth = list(range(2,10))
hyper_param = {'fit__alpha':alphas}
params_RF = {'fit__n_estimators':[5,10],
             'fit__max_depth':[1, 5, 10, 15]}
params_DT= {'fit__max_depth':depth, 
            'fit__min_samples_split': [0.1, 1]}


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Оптимизация гиперпараметров выполнена формально: используя список в сетке параметров, мы исследуем только те значения, которые непосредственно находятся в этом списке - так шанс найти оптимальные гиперпараметры крайне низок. Вместо списка из нескольких значений стоит использовать последовательность `range()` - так шанс найти оптимальное значение выше.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[53]:


model_Lasso_rougher = Pipeline([('scaler', MinMaxScaler()), ('fit', Lasso(random_state=12345))])
model_Lasso_final = Pipeline([('scaler', MinMaxScaler()), ('fit', Lasso(random_state=12345))])


# In[54]:


model_DTR_rougher = Pipeline([('scaler', MinMaxScaler()), ('fit', DecisionTreeRegressor(random_state=12345))])
model_DTR_final = Pipeline([('scaler', MinMaxScaler()), ('fit', DecisionTreeRegressor(random_state=12345))])


# In[55]:


model_EN_rougher =  Pipeline([('scaler', MinMaxScaler()), ('fit', ElasticNet(random_state=12345))])
model_EN_final =  Pipeline([('scaler', MinMaxScaler()), ('fit', ElasticNet(random_state=12345))])


# In[56]:


model_RFR_rougher = Pipeline([('scaler', MinMaxScaler()), ('fit', RandomForestRegressor(random_state=12345))])
model_RFR_final = Pipeline([('scaler', MinMaxScaler()), ('fit', RandomForestRegressor(random_state=12345))])


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# У моделей не настроен `random_state`.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Напишем функцию для подсчета метрики RMSE, которую будем использовать для скоринга по время поиске по сетке лучших параметров моделей.

# In[57]:


def rmse(target, predict):
    
    target = np.array(target)
    predict = np.array(predict)
    diff = predict-target
    square_diff = diff ** 2
    mean_square_diff = square_diff.mean()
    rmse = np.sqrt(mean_square_diff)
    return rmse


# In[58]:


scoring = {'rmse': make_scorer(rmse, greater_is_better=False),
            'mae': 'neg_mean_absolute_error',
           'sMape': make_scorer(sMAPE_i, greater_is_better=False)
          }


# In[59]:


model_rougher_Lasso = GridSearchCV(model_Lasso_rougher, param_grid=hyper_param, 
                                   scoring=scoring, refit='sMape',return_train_score=True).fit(feature, target_rougher)
model_final_Lasso = GridSearchCV(model_Lasso_final, param_grid=hyper_param, 
                                scoring=scoring, refit='sMape',return_train_score=True).fit(feature, target_final)


# In[60]:


model_rougher_DTR = GridSearchCV(model_DTR_rougher, param_grid=params_DT, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_rougher)
model_final_DTR = GridSearchCV(model_DTR_final, param_grid=params_DT, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_final)


# In[61]:


model_rougher_ElasticNet= GridSearchCV(model_EN_rougher, param_grid=hyper_param, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_rougher)
model_final_ElasticNet= GridSearchCV(model_EN_final, param_grid=hyper_param, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_final)


# In[62]:


model_rougher_RFR = GridSearchCV(model_RFR_rougher, param_grid=params_RF, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_rougher)


# In[63]:


model_final_RFR = GridSearchCV(model_RFR_final, param_grid=params_RF, 
                                 refit='sMape', scoring=scoring,return_train_score=True).fit(feature, target_final)


# Выведем на экран лучшие гиперпараметры моделей и значения оценщика.

# In[80]:


print("Лучшие параметры и скоринги моделей\n")
print("Флотация")
print("Регрессия Лассо:", model_rougher_Lasso.cv_results_['params'][model_rougher_Lasso.best_index_])
print('rmse =', abs(model_rougher_Lasso.cv_results_['mean_test_rmse'][model_rougher_Lasso.best_index_]))
print('mae =', abs(model_rougher_Lasso.cv_results_['mean_test_mae'][model_rougher_Lasso.best_index_]))
print("Решающее дерево", model_rougher_DTR.cv_results_['params'][model_rougher_DTR.best_index_])
print('rmse =', abs(model_rougher_DTR.cv_results_['mean_test_rmse'][model_rougher_DTR.best_index_]))
print('mae =', abs(model_rougher_DTR.cv_results_['mean_test_mae'][model_rougher_DTR.best_index_]))
print("Эластичная сеть", model_rougher_ElasticNet.cv_results_['params'][model_rougher_ElasticNet.best_index_])
print('rmse =', abs(model_rougher_ElasticNet.cv_results_['mean_test_rmse'][model_rougher_ElasticNet.best_index_]))
print('mae =', abs(model_rougher_ElasticNet.cv_results_['mean_test_mae'][model_rougher_ElasticNet.best_index_]))
print("Случайный лес", model_rougher_RFR.cv_results_['params'][model_rougher_RFR.best_index_])
print('rmse =', abs(model_rougher_RFR.cv_results_['mean_test_rmse'][model_rougher_RFR.best_index_]))
print('mae =', abs(model_rougher_RFR.cv_results_['mean_test_mae'][model_rougher_RFR.best_index_]))

print("\nФинальная очистка")
print("Регрессия Лассо", model_final_Lasso.cv_results_['params'][model_final_Lasso.best_index_])
print('rmse =', abs(model_rougher_Lasso.cv_results_['mean_test_rmse'][model_final_Lasso.best_index_]))
print('mae =', abs(model_rougher_Lasso.cv_results_['mean_test_mae'][model_final_Lasso.best_index_]))
print("Решающее дерево", model_final_DTR.cv_results_['params'][model_final_DTR.best_index_])
print('rmse =', abs(model_final_DTR.cv_results_['mean_test_rmse'][model_final_DTR.best_index_]))
print('mae =', abs(model_final_DTR.cv_results_['mean_test_mae'][model_final_DTR.best_index_]))
print("Эластичная сеть", model_final_ElasticNet.cv_results_['params'][model_final_ElasticNet.best_index_])
print('rmse =', abs(model_final_ElasticNet.cv_results_['mean_test_rmse'][model_final_ElasticNet.best_index_]))
print('mae =', abs(model_final_ElasticNet.cv_results_['mean_test_mae'][model_final_ElasticNet.best_index_]))
print("Случайный лес", model_final_RFR.cv_results_['params'][model_final_RFR.best_index_])
print('rmse =', abs(model_final_RFR.cv_results_['mean_test_rmse'][model_final_RFR.best_index_]))
print('mae =', abs(model_final_RFR.cv_results_['mean_test_mae'][model_final_RFR.best_index_]))


# In[65]:


print('sMAPE на обучающей выборке:')
print("Регрессия Лассо",0.25*abs(model_rougher_Lasso.best_score_)+0.75*abs(model_final_Lasso.best_score_))
print("Решающее дерево",0.25*abs(model_rougher_DTR.best_score_)+0.75*abs(model_final_DTR.best_score_))
print("Эластичная сеть",0.25*abs(model_rougher_ElasticNet.best_score_)+0.75*abs(model_final_ElasticNet.best_score_))
print("Случайный лес",0.25*abs(model_rougher_RFR.best_score_)+0.75*abs(model_final_RFR.best_score_))


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Не посчитаны итоговые оценки для каждой модели.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
#     
# 1. При взвешивании использованы неправильные веса - см.условие проекта.
# 2. Не выведены метрики `MAE` и `RMSE` - см.условие допзадания о том, как нужно их получить из `cv_results_`.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Лучший результат для оценки эффективности обогащения чернового концентрата показала модель ElasticNet, в то время как для оценки эффективности обогащения финального концентрата наиболее точной оказалась модель Lasso. Итоговая метрика sMAPE достигла минимального значения у модели ElasticNet.

# ## Проверка лучшей модели на тестовой выборке.

# In[66]:


target=full[['date','rougher.output.recovery','final.output.recovery']]
test=test.merge(target,on=['date'], how='left')


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> В `test` добавили целевые признаки из `full`, используя дату как ключ при соединении - отлично!

# In[67]:


test=test.dropna()
target_test_rougher=test['rougher.output.recovery']
target_test_final=test['final.output.recovery']
feature_test=test.drop(['date','rougher.output.recovery','final.output.recovery'], axis=1)


# In[68]:


prediction_rougher=model_rougher_ElasticNet.predict(feature_test)
prediction_final=model_final_ElasticNet.predict(feature_test)


# In[69]:


print('sMAPE на тестовой выборке:')
sMAPE(sMAPE_i(target_test_rougher, prediction_rougher), sMAPE_i(target_test_final, prediction_final))


# На тестовой выборке метрика sMAPE получила значение ниже, чем на обучающей. Модель выбрана корректно.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На `test` оцениваем только одну модель, лучшую по итогам кросс-валидации. Эта концепция находит своё отражение в условиях эксплуатации модели в реальной среде: в промышленной эксплуатации не работает несколько моделей одновременно - в промышленную эксплуатацию запускают только одну модель, которая была выбрана из нескольких в ходе промежуточной оценки. Так же и здесь - тестовая выборка имитирует поток реальных данных, и с этим потоком должна работать только одна модель.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Очень важно также проверить лучшую модель на адекватность, сравнив качество её предсказаний с качеством модели, которая предсказывала бы константу - вдруг окажется, что не было бы большого смысла заниматься созданием новых признаков, тюнингом и кросс-валидацией моделей, если можно было бы просто предсказывать среднее значение тренировочной выборки? 
#     
# В качестве константной модели можно использовать `DummyRegressor` (https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html) -  эта модель как раз создана для генерирования константных предсказаний.
#     
# Важно, чтобы результат тестирования нашей модели на тествой выборке был лучше, чем результат константной модели - в противном случае наша модель является бесполезной, так как все наши усилия над проектом не принесли результата, а можель, просто предсказывющая среднее на `train`, делает нашу работу лучше.
#     

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.
#     

# ## Сравнение с константной моделью.

# Проверим наши модели на адекватность.

# In[70]:


dummy_regressor_rougher = DummyRegressor(strategy="mean")
dummy_regressor_rougher.fit(feature, target_rougher)
dummy_rougher_pred = dummy_regressor_rougher.predict(prediction_rougher)
smape_dummy_rougher = sMAPE_i(target_test_rougher, dummy_rougher_pred)
smape_dummy_rougher


# In[71]:


dummy_regressor_final = DummyRegressor(strategy="mean")
dummy_regressor_final.fit(feature, target_final)
dummy_final_pred = dummy_regressor_final.predict(prediction_final)
smape_dummy_final = sMAPE_i(target_test_final, dummy_final_pred)
smape_dummy_final


# In[72]:


smape_dummy = (smape_dummy_final + smape_dummy_rougher)/2
smape_dummy


# Наша модель предсказывает лучше, чем константная со средним значением признака.

# ## Выводы.

# - Изучив исходные данные мы определили, что в полной и обучающей выборках по 87 столбцов, в тестовой 53. В данных есть пропуски. Некоторые параметры недоступны, потому что замеряются и/или рассчитываются значительно позже. Из-за этого в тестовой выборке отсутствуют некоторые признаки, которые могут быть в обучающей.
# - Проверив, правильно ли рассчитана эффективность обогащения рассчитана. Вычислили её на обучающей выборке для признака rougher.output.recovery и нашли MAE между нашими расчётами и значением признака близкое к нулю, что позволило сделать вывод о корректности расчетов эффективности обогащения.
# - Отсутствующими столбцами в тестовой выборке оказались выходные признаки после каждого технологического этапа.Среди них и наши целевые признаки final.output.recovery и rougher.output.recovery.
# - В процессе предобработки данных были обнаружены пропуски в выходных значениях технологических этапов. По условиям задачи соседние по времени параметры часто похожи. Мы заполнили пропуски значениями, стоящими на строку выше пропущенных.
# - При помощи "ящиков с усами" мы определили, что больше всего выбросов в концентрации золота (AU) на стадиях первичной и финальной очистки. А так же обнаружили, что среднее значение концентрации золота на финальной очистке выросло более чем в 2 раза по сравнению с первым этапом флотации. Отфильтровали выбросы в обучающей выборке.
# - Исследовав концентрацию металлов на каждом этапе обработки, можно заметить, что после флотации содержание металлов возросло на 20% по сравнению с сырьем, после первичной очистки концетрация металлов снижается в среднем на 7-8 %, зато после финальной очистки вырастает на 7-8%, и как нам известно из анализа выше, в основном за счет увеличения концентрации золота.
# - Сранив входные данные мы заметили, что размеры гранул сырья в обучающей и тестовой выборках распределяются идентичным образом.
# - Использовав кросс-валидацию при обучении моделей Линейной регрессии, Лассо, Решающего дерева, Эластичной сети и Случайного леса, нами был выбраны для дальнейшего использования Эластичная сеть (исследование после этапа флотации) и Лассо (для финальной очитски), т.к. именно они показали наилучшие параметра качества sMAPE на обучающей выборке. На тестовой выборке выбранные модели показали хорошие результаты оценки качества. Проверка на адекватность константной моделью проведена успешно.
# 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть итоговый вывод - отлично!

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту.
# 
# Татьяна, проект получился на довольно хорошем уровне - отличная работа над проектом, молодец!
# 
# Мне нравится твой аналитический подход к выполнению проекта, ты соблюдаешь структуру работы, выполняешь её последовательно - это очень хорошо! Шаги проекта выполнены по порядку согласно плану проекта, нет смысловых и структурных ям. Важно, что не забываешь про выводы.
# 
# Работа с моделями также выполнена отлично: исследовано несколько алгоритмов, проведён подбор гиперпараметров, выполнена промежуточная оценка моделей на кросс-валидации - молодец!
#     
# Над проектом ещё стоит поработать - есть рекомендации по дополнению некоторых твоих шагов проекта. Такие рекомендации я отметил жёлтыми комментариями. Будет здорово, если ты учтёшь их - так проект станет структурно и содержательно более совершенным.
#     
# Также в работе есть критические замечания. К этим замечаниям я оставил пояснительные комментарии красного цвета, в которых перечислил возможные варианты дальнейших действий. Уверен, ты быстро с этим управишься:)
#     
# Если о том, что нужно сделать в рамках комментариев, будут возникать вопросы - оставь их, пожалуйста, в комментариях, и я отвечу на них во время следующего ревью.
#     
# Также буду рад ответить на любые твои вопросы по проекту или на какие-либо другие, если они у тебя имеются - оставь их в комментариях, и я постараюсь ответить:)
#     
# Жду твой проект на повторном ревью. До встречи:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.2.
# 
# Татьяна, продолжаем работу над проектом - актуальные замечания отмечены комментариями с меткой `v.2`.
#     
# Жду тебя снова:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.3.
# 
# Татьяна, продолжаем работу над проектом - актуальные замечания отмечены комментариями с меткой `v.3`.
#     
# Жду тебя снова:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.4.
# 
# Татьяна, все замечания учтены - проект принят!
#     
# Спасибо за хорошую работу над проектом, желаю успехов в дальнейшем обучении:)
