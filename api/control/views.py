from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.control.serializers import BMIInputSerializer, BloodPressureInputSerializer, PulseInputSerializer, \
    FluidInputSerializer, MNOControlSerializer, LipidSerializer


class BMICalculator(APIView):
    """
    Калькулятор контроля веса индекса массы тела
    """
    serializer_class = BMIInputSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        weight = serializer.validated_data['weight']
        height = serializer.validated_data['height']
        bmi = weight / (height * height)

        return Response({'bmi': bmi})


class BloodPressureCalculator(APIView):
    """
    Калькулятор контроля артериального давления
    """
    serializer_class = BloodPressureInputSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        systolic = serializer.validated_data['systolic']
        diastolic = serializer.validated_data['diastolic']
        pulse_pressure = systolic - diastolic
        mean_arterial_pressure = diastolic + (pulse_pressure / 3)

        return Response({
            'систолический': systolic,
            'диастолический': diastolic,
            'пульсовое_давление': pulse_pressure,
            'среднее_артериальное_давление': mean_arterial_pressure,
        })


class PulseCalculator(APIView):
    """
    Калькулятор контроля пульса
    """
    serializer_class = PulseInputSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        pulse = serializer.validated_data['pulse']
        cycle_duration = serializer.validated_data['cycle_duration']
        pulse_control = (60 * pulse) / cycle_duration

        return Response({
            'пульс': pulse,
            'продолжительность_цикла': cycle_duration,
            'импульсный_контроль': pulse_control,
        })


class FluidCalculator(APIView):
    """
    Контроль выпитой жидкости и выделенной жидкости
    """
    serializer_class = FluidInputSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        fluid_intake = serializer.validated_data['fluid_intake']
        fluid_output = serializer.validated_data['fluid_output']
        fluid_balance = fluid_intake - fluid_output

        return Response({
            'потребление_жидкости': fluid_intake,
            'выход_жидкости': fluid_output,
            'баланс_жидкости': fluid_balance,
        })


def mno_control(mno):
    if mno < 2.0:
        return "Ниже нормы"
    elif mno >= 2.0 and mno <= 3.0:
        return "В норме"
    else:
        return "Выше нормы"


class MnoControlView(APIView):
    """
    Показатель нормы МНО при приеме варфарина
    """
    serializer_class = MNOControlSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            mno = serializer.validated_data['mno']
            control = mno_control(mno)
            return Response({'control': control}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LipidProfileView(APIView):
    """
    Дипидный профиль
    """
    serializer_class = LipidSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        cholesterol = serializer.validated_data['cholesterol']
        ldl = serializer.validated_data['ldl']
        hdl = serializer.validated_data['hdl']
        triglycerides = serializer.validated_data['triglycerides']

        total_cholesterol = cholesterol + ldl + hdl + (triglycerides / 5)
        ldl_c = cholesterol + (triglycerides / 5) - hdl - (ldl / 2.2)
        non_hdl_c = total_cholesterol - hdl

        lipid_profile = {
            'общий_холестерин': round(total_cholesterol, 2),
            'холестерин_липопротеидов_низкой_плотности,': round(ldl_c, 2),
            'холестерин_липопротеинов_не_высокой_плотности': round(non_hdl_c, 2),
            'липопротеины_высокой_плотности_холестерина': round(hdl, 2),
            'триглицериды': round(triglycerides, 2)
        }

        return Response(lipid_profile)
