from django.shortcuts import render
from django.views import View
from .models import DiceRoll
from .forms import DiceRollForm
import random


class DiceRollView(View):
    def get(self, request):
        form = DiceRollForm()
        rolls = DiceRoll.objects.all().order_by('-timestamp')[:10]
        return render(request, 'dice_roller.html', {'form': form, 'rolls': rolls})
    
    def post(self, request):
        form = DiceRollForm(request.POST)
        if form.is_valid():
            dice = form.cleaned_data['dice']
            sides = form.cleaned_data['sides']
            option = form.cleaned_data['option']
            dice_pool = []
            result_pool = []
            for _ in range(dice):
                roll = random.randint(1, sides)
                dice_pool.append(roll)
                if (option == 'gwf'):
                    if (roll <= 2):
                        roll = random.randint(1, sides)
                if (option == 'ea'):
                    if (roll == 1):
                        roll = 2
                result_pool.append(roll)
            result = sum(result_pool)
            DiceRoll.objects.create(roll=roll, option=option, result=result)
            rolls = DiceRoll.objects.all().order_by('-timestamp')[:10]
            return render(request, 'dice_roller.html', {
                'form': form, 
                'roll': roll, 
                'result': result, 
                'rolls': rolls, 
                'dice': dice, 
                'sides': sides, 
                'option': option,
                'dice_pool': dice_pool,
                'result_pool': result_pool
                })
        
        else:
            rolls = DiceRoll.objects.all().order_by('-timestamp')[:10]
            return render(request, 'dice_roller.html', {'form': form, 'rolls': rolls})

