# banana_api/tests/test_diseases_api.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker

from banana_api.models import Disease


class DiseaseApiTests(APITestCase):
    def setUp(self):
        # สร้างตัวอย่างข้อมูล 25 records สำหรับทดสอบ pagination
        self.diseases = baker.make(Disease, _quantity=25)

    def test_list_diseases_default_pagination(self):
        """
        GET /api/diseases/ ควรคืน 200 และมี keys: count, total_pages, current_page, page_size, results
        ค่า default page=1, size=10
        """
        url = reverse('disease_list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        body = res.json()

        for key in ["count", "total_pages", "current_page", "page_size", "results"]:
            self.assertIn(key, body)

        self.assertEqual(body["count"], 25)
        self.assertEqual(body["current_page"], 1)
        self.assertEqual(body["page_size"], 10)
        self.assertEqual(len(body["results"]), 10)

    def test_list_diseases_custom_page_and_size(self):
        """
        GET /api/diseases/?page=2&size=7 → page 2 จะได้ 7 records
        """
        url = reverse('disease_list')
        res = self.client.get(url, {"page": 2, "size": 7})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        body = res.json()
        self.assertEqual(body["current_page"], 2)
        self.assertEqual(body["page_size"], 7)
        self.assertEqual(len(body["results"]), 7)

    def test_list_diseases_invalid_query_params_return_400(self):
        """
        ถ้า get_pagination_params() โยน BadRequest (เช่น page/size ผิดรูปแบบ) 
        ควรได้ 400 ผ่าน custom exception handler ของโปรเจกต์
        """
        url = reverse('disease_list')
        res = self.client.get(url, {"page": "abc", "size": "-5"})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_disease_detail_ok(self):
        """
        GET /api/diseases/<pk>/ → 200 และมีฟิลด์หลักของ Disease (แล้วแต่ serializer)
        """
        obj = self.diseases[0]
        url = reverse('disease_detail', args=[obj.pk])
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.json()
        # เช็คอย่างน้อยว่าคืน pk เดียวกัน (serializer อาจจะใช้ 'id' หรือ field อื่น)
        # ถ้า serializer ใช้ 'id':
        self.assertIn("id", data)
        self.assertEqual(data["id"], obj.id)

    def test_get_disease_detail_404(self):
        """
        ถ้า pk ไม่มีอยู่ ควรได้ 404
        """
        url = reverse('disease_detail', args=[999999])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
