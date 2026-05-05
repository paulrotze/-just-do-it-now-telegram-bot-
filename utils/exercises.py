"""
Утилиты для работы с упражнениями.
Вынесенная общая логика для устранения дублирования кода.
"""
import random
from typing import Dict, List


def get_gym_exercise(muscle_group: str, level: str, gym_workouts: Dict) -> str:
    """
    Получить случайное упражнение для группы мышц и уровня.
    
    Args:
        muscle_group: Группа мышц (chest, back, legs, shoulders, arms)
        level: Уровень сложности (pro1, pro2, pro3)
        gym_workouts: Словарь с упражнениями из config
    
    Returns:
        Строка с описанием упражнения
    """
    if level == "pro1":
        return random.choice(gym_workouts[muscle_group]["pro1"])
    elif level == "pro2":
        combined = gym_workouts[muscle_group]["pro1"] + gym_workouts[muscle_group]["pro2"]
        return random.choice(combined)
    elif level == "pro3":
        combined = (gym_workouts[muscle_group]["pro1"] +
                    gym_workouts[muscle_group]["pro2"] +
                    gym_workouts[muscle_group]["pro3"])
        return random.choice(combined)
    else:
        return random.choice(gym_workouts[muscle_group]["pro1"])


def get_workout_by_level(goal: str, level: str, workouts: Dict) -> str:
    """
    Получить случайное задание по цели и уровню.
    
    Args:
        goal: Цель пользователя (lose_weight, gain_mass, get_fit)
        level: Уровень сложности (easy, normal, hard, pro1, pro2, pro3)
        workouts: Словарь с заданиями из config
    
    Returns:
        Строка с описанием задания
    """
    if level in ["pro1", "pro2", "pro3"]:
        return random.choice(workouts[goal]["hard"])
    elif level == "hard":
        combined = workouts[goal]["normal"] + workouts[goal]["hard"]
        return random.choice(combined)
    else:
        return random.choice(workouts[goal][level])
