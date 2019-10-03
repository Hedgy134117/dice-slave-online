from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SheetGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def sheetGroupName(self):
        return str(self.name)

class Sheet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100)

    # for sheetGroup in SheetGroup.objects.all().order_by('name'):
    #     groupOptions.append((sheetGroup.name, sheetGroup.name))

    sheetGroup = models.ManyToManyField(SheetGroup)

    slug = models.SlugField(default="")

    Class = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    xp = models.IntegerField()
    level = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    strengthMod = models.IntegerField()
    dexterityMod = models.IntegerField()
    constitutionMod = models.IntegerField()
    intelligenceMod = models.IntegerField()
    wisdomMod = models.IntegerField()
    charismaMod = models.IntegerField()

    sStrength = models.BooleanField(verbose_name="Saving Throw: Strength")
    sDexterity = models.BooleanField(verbose_name="Saving Throw: Dexterity")
    sConstitution = models.BooleanField(verbose_name="Saving Throw: Constitution")
    sIntelligence = models.BooleanField(verbose_name="Saving Throw: Intelligence")
    sWisdom = models.BooleanField(verbose_name="Saving Throw: Wisdom")
    sCharisma = models.BooleanField(verbose_name="Saving Throw: Charisma")

    acrobatics = models.BooleanField()
    animalHandling = models.BooleanField()
    arcana = models.BooleanField()
    athletics = models.BooleanField()
    deception = models.BooleanField()
    history = models.BooleanField()
    insight = models.BooleanField()
    intimidation = models.BooleanField()
    investigation = models.BooleanField()
    medicine = models.BooleanField()
    nature = models.BooleanField()
    perception = models.BooleanField()
    performance = models.BooleanField()
    persuasion = models.BooleanField()
    religion = models.BooleanField()
    sleightOfHand = models.BooleanField()
    stealth = models.BooleanField()
    survival = models.BooleanField()

    acrobaticsMod = models.IntegerField()
    animalHandlingMod = models.IntegerField()
    arcanaMod = models.IntegerField()
    deceptionMod = models.IntegerField()
    historyMod = models.IntegerField()
    insightMod = models.IntegerField()
    intimidationMod = models.IntegerField()
    investigationMod = models.IntegerField()
    medicineMod = models.IntegerField()
    natureMod = models.IntegerField()
    perceptionMod = models.IntegerField()
    performanceMod = models.IntegerField()
    persuasionMod = models.IntegerField()
    religionMod = models.IntegerField()
    sleightOfHandMod = models.IntegerField()
    stealthMod = models.IntegerField()
    survivalMod = models.IntegerField()

    otherProficiencies = models.CharField(max_length=250)
    languages = models.CharField(max_length=250)
    equipment = models.CharField(max_length=250)
    copper = models.IntegerField()
    silver = models.IntegerField()
    gold = models.IntegerField()
    platinum = models.IntegerField()

    armorClass = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()
    maxHitPoints = models.IntegerField()
    hitPoints = models.IntegerField()
    hitDice = models.CharField(max_length=250)
    sDeathSave1 = models.BooleanField(default=False)
    sDeathSave2 = models.BooleanField(default=False)
    sDeathSave3 = models.BooleanField(default=False)
    fDeathSave1 = models.BooleanField(default=False)
    fDeathSave2 = models.BooleanField(default=False)
    fDeathSave3 = models.BooleanField(default=False)

    personalityTraits = models.CharField(max_length=250)
    ideals = models.CharField(max_length=250)
    bonds = models.CharField(max_length=250)
    flaws = models.CharField(max_length=250)
    featuresTraits = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def sheetGroupValue(self):
        groups = ''
        for group in self.sheetGroup.all():
            groups += group.name + " "

        return groups[0:len(groups)-1]